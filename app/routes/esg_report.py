from flask import Blueprint, jsonify, request
from langchain_community.chat_models import ChatPerplexity
from langchain_core.prompts import ChatPromptTemplate
from app.config.settings import config
from app.core.report_prompt import (
    get_report_prompt_financial,
    get_report_prompt_boolean,
    get_report_prompt_miscellaneous
)
from app.enums.data_field import (
    financial_fields,
    gsg_fields,
    boolean_fields,
    miscellaneous_fields
)
import json
import asyncio
import time
from app.database_services.insert_schema import (
    insert_or_update_company_report,
    insert_company_report_table_without_year
)



esg_report_bp = Blueprint('esg_report', __name__)


# Global rate limiting variables
request_count = 0
last_reset_time = time.time()

# Rate limit parameters
MAX_REQUESTS_PER_MINUTE = 50
RATE_LIMIT_PERIOD = 60  # 60 seconds



@esg_report_bp.route('/total_data', methods=['GET'])
def get_total_data():
    total_len = len(financial_fields) + len(gsg_fields) + len(boolean_fields) + len(miscellaneous_fields)
    return jsonify({'total_data': total_len})


# Helper function to manage rate limit
def enforce_rate_limit():
    global request_count, last_reset_time

    current_time = time.time()
    time_since_last_reset = current_time - last_reset_time

    if time_since_last_reset >= RATE_LIMIT_PERIOD:
        # Reset the count after 1 minute
        request_count = 0
        last_reset_time = current_time

    if request_count >= MAX_REQUESTS_PER_MINUTE:
        # Introduce a delay if the limit is reached
        sleep_time = RATE_LIMIT_PERIOD - time_since_last_reset
        time.sleep(sleep_time)
        request_count = 0  # Reset after sleep

    request_count += 1  # Increment the request counter




async def process_field(chat, field, company_name, prompt_template, is_financial=True):
    query = f"{field['query']}".format(company_name=company_name)
    expected_value = field['expected_value']
    data_field = field['data_field']

    prompt = ChatPromptTemplate.from_messages([("human", prompt_template())])
    chain = prompt | chat

    try:
        response = await chain.ainvoke({
            "query": query,
            "expected_value": expected_value
        })

        if response and response.content:
            data = json.loads(response.content)
            if data.get("available").upper() == "YES":
                if is_financial:
                    await insert_or_update_company_report(company_name, data_field, data["response"])
                else:
                    await insert_company_report_table_without_year(company_name, data_field, data["response"])
                return data_field, data["response"], data
            return data_field, "", None
    except Exception as e:
        return data_field, "", None



@esg_report_bp.route('/get_financial_report', methods=['POST'])
def get_financial_report():
    company_name = request.json.get('company_name')
    if not company_name:
        return jsonify({'error': 'Company name is required'}), 400
    
    # Enforce rate limit before processing
    enforce_rate_limit()

    chat = ChatPerplexity(
        temperature=0,
        pplx_api_key=config.PERPLEXITY_API_KEY,
        model="llama-3.1-sonar-small-128k-online"
    )
    
    async def process_financial_fields():
        try:
            responses_data = []
            csv_data = []
            
            # Process financial fields concurrently
            financial_tasks = [
                process_field(chat, field, company_name, get_report_prompt_financial, True)
                for field in financial_fields
            ]

            # Gather financial results
            financial_results = await asyncio.gather(*financial_tasks)

            # Process results
            for data_field, response, data in financial_results:
                csv_data.append([data_field, response])
                if data and isinstance(data["response"], list):
                    responses_data.extend(data["response"])

            return responses_data

        except Exception as e:
            raise

    # Run the async function using asyncio
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        responses_data = loop.run_until_complete(process_financial_fields())
        return jsonify(responses_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    finally:
        loop.close()



@esg_report_bp.route('/get_esg_report', methods=['POST'])
def get_esg_report():
    company_name = request.json.get('company_name')
    if not company_name:
        return jsonify({'error': 'Company name is required'}), 400
    
    # Enforce rate limit before processing
    enforce_rate_limit()

    chat = ChatPerplexity(
        temperature=0,
        pplx_api_key=config.PERPLEXITY_API_KEY,
        model="llama-3.1-sonar-small-128k-online"
    )
    
    async def process_other_fields():
        try:
            responses_data = []
            csv_data = []
            
            # Process all other fields concurrently
            gsg_tasks = [
                process_field(chat, field, company_name, get_report_prompt_financial, True)
                for field in gsg_fields
            ]
            boolean_tasks = [
                process_field(chat, field, company_name, get_report_prompt_boolean, False)
                for field in boolean_fields
            ]
            misc_tasks = [
                process_field(chat, field, company_name, get_report_prompt_miscellaneous, False)
                for field in miscellaneous_fields
            ]

            # Gather all results
            all_results = await asyncio.gather(
                *gsg_tasks,
                *boolean_tasks,
                *misc_tasks
            )

            # Process results
            for data_field, response, data in all_results:
                csv_data.append([data_field, response])
                if data:
                    if isinstance(data["response"], list):
                        responses_data.extend(data["response"])
                    else:
                        responses_data.append(data)

            return responses_data

        except Exception as e:
            raise

    # Run the async function using asyncio
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        responses_data = loop.run_until_complete(process_other_fields())
        return jsonify(responses_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    finally:
        loop.close()
