from flask import Blueprint, jsonify
import asyncio
from app.database_services.fetch_data import fetch_data_by_company_name
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