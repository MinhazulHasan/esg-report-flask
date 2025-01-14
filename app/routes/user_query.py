from flask import Blueprint, jsonify, request
from app.core.report_prompt import get_user_query_prompt
from langchain_community.chat_models import ChatPerplexity
from langchain_core.prompts import ChatPromptTemplate
from app.config.settings import config
from flask import abort



user_query_bp = Blueprint('user_query', __name__)


def validate_response(response):
    if not response or not response.content:
        abort(404, description="No response found!")
    return response.content


@user_query_bp.route("/get_query_result", methods=["POST"])
def get_query_result():
    data = request.get_json()
    print("data", data)
    
    if not data or 'query' not in data:
        abort(400, description="Query parameter is required in the request body.")
    
    query = data['query']
    
    try:
        chat = ChatPerplexity(
            temperature=0,
            pplx_api_key=config.PERPLEXITY_API_KEY,
            model="llama-3.1-sonar-small-128k-online"
        )

        prompt = ChatPromptTemplate.from_messages([("human", get_user_query_prompt())])
        chain = prompt | chat

        response = chain.invoke({"query": query})
        response_content = validate_response(response)
        return jsonify(response_content), 200

    except Exception as e:
        abort(500, description="Internal server error.")
