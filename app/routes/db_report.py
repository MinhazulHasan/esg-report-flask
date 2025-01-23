from flask import Blueprint, jsonify, request
import asyncio
from app.database_services.fetch_data import fetch_data_by_company_name, fetch_data_by_data_field
from app.utilities.utils import group_and_sort_data_by_data_field


db_report_bp = Blueprint('db_report', __name__)

@db_report_bp.route('/company/<company_name>', methods=['GET'])
def get_company_data(company_name):
    try:
        # Run async function in sync context
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            data = loop.run_until_complete(fetch_data_by_company_name(company_name))
        finally:
            loop.close()

        if not data:
            return jsonify({'error': 'No data found for the specified company'}), 404
            
        grouped_data = group_and_sort_data_by_data_field(data)
        return jsonify(grouped_data)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500



@db_report_bp.route('/company/data_point_report', methods=['POST'])
def get_data_point_report():
    if not request.is_json:
        return jsonify({'error': 'Request must be JSON'}), 400
    
    data = request.get_json()
    if not data or 'company_name' not in data or 'data_point' not in data:
        return jsonify({'error': 'Company name and data point parameters are required in the request body'}), 400

    company_name = data['company_name']
    data_point = data['data_point']
    year = data.get('year')

    try:
        result = asyncio.run(fetch_data_by_data_field(company_name, data_point, year))
        if not result:
            return jsonify({'error': 'No data found for the specified parameters'}), 404

        return jsonify({ 'company_name': company_name, 'data_point': data_point, 'response': result })

    except Exception as e:
        return jsonify({'error': str(e)}), 500
