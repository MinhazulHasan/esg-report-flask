import asyncio
from app.routes.esg_report import process_field
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
from app.config.settings import config
from langchain_community.chat_models import ChatPerplexity
import time
from tenacity import retry, stop_after_attempt, wait_exponential

companies = [
    "Apple Inc",
    "JPMorgan Chase & Co",
    "Bank of America Corporation",
    "Citigroup Inc",
    "Wells Fargo & Company",
    "The Goldman Sachs Group",
    "Morgan Stanley",
    "Alphabet Inc"
]


@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
async def update_company_data(company_name):
    chat = ChatPerplexity(
        temperature=0,
        pplx_api_key=config.PERPLEXITY_API_KEY,
        model="llama-3.1-sonar-small-128k-online"
    )
    
    try:
        # Process financial fields
        financial_tasks = [
            process_field(chat, field, company_name, get_report_prompt_financial, True)
            for field in financial_fields
        ]
        financial_results = await asyncio.gather(*financial_tasks)

        # Introduce delay between API calls
        await asyncio.sleep(60)

        # Process ESG and other fields
        other_tasks = [
            *[
                process_field(chat, field, company_name, get_report_prompt_financial, True)
                for field in gsg_fields
            ],
            *[
                process_field(chat, field, company_name, get_report_prompt_boolean, False)
                for field in boolean_fields
            ],
            *[
                process_field(chat, field, company_name, get_report_prompt_miscellaneous, False)
                for field in miscellaneous_fields
            ]
        ]
        other_results = await asyncio.gather(*other_tasks)

        # Additional delay after processing each company
        await asyncio.sleep(60)

        return financial_results + other_results
    
    except Exception as e:
        print(f"Error: {e}")



def update_all_companies():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        for company in companies:
            loop.run_until_complete(update_company_data(company))
            # Delay between companies
            time.sleep(60)

    except Exception as e:
        print(f"Error in monthly update: {str(e)}")

    finally:
        loop.close()
