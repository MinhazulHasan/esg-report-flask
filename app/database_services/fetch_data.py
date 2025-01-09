from app.database_services.db_utils import get_connection
from app.utilities.logger import report_logger



async def fetch_data_by_company_name(company_name: str):
    query = """
        SELECT data_field, year, response, reported_at
        FROM ESGReport
        WHERE company_name = ?
    """
    
    try:
        async with await get_connection() as conn:
            async with conn.cursor() as cursor:
                await cursor.execute(query, (company_name,))
                rows = await cursor.fetchall()
                
                # Log success
                if rows:
                    report_logger.info(f"Data fetched successfully for company: {company_name}.")
                else:
                    report_logger.warning(f"No data found for company: {company_name}.")
                
                # Convert to list of dictionaries
                columns = [desc[0] for desc in cursor.description]
                return [dict(zip(columns, row)) for row in rows]
    
    except Exception as e:
        report_logger.error(
            f"From DATABASE Service:\n"
            f"Error fetching data for {company_name}.\n"
            f"Error: {e}"
        )
        return None
    
    finally:
        await cursor.close()
        await conn.close()
