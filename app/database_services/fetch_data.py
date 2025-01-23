from app.database_services.db_utils import get_connection

async def fetch_data_by_company_name(company_name: str):
    query = """
        SELECT data_field, year, response, reported_at
        FROM ESGReport
        WHERE company_name = ?
    """
    
    conn = None
    cursor = None
    try:
        conn = await get_connection()
        cursor = await conn.cursor()
        await cursor.execute(query, (company_name,))
        rows = await cursor.fetchall()
        
        # Log success
        if rows:
            print(f"Data fetched successfully for company: {company_name}.")
        else:
            print(f"No data found for company: {company_name}.")
        
        # Convert to list of dictionaries
        columns = [desc[0] for desc in cursor.description]
        return [dict(zip(columns, row)) for row in rows]
    
    except Exception as e:
        print(
            f"From DATABASE Service:\n"
            f"Error fetching data for {company_name}.\n"
            f"Error: {e}"
        )
        return None
    
    finally:
        if cursor:
            await cursor.close()
        if conn:
            await conn.close()



async def fetch_data_by_data_field(company_name: str, data_field: str, year: str = None):
    query = """
        SELECT response, reported_at
        FROM ESGReport
        WHERE company_name = ? AND data_field = ?
    """

    if year:
        query += " AND year = ?"

    conn = None
    cursor = None

    try:
        conn = await get_connection()
        cursor = await conn.cursor()

        params = (company_name, data_field) if not year else (company_name, data_field, year)
        await cursor.execute(query, params)
        rows = await cursor.fetchall()

        if rows:
            print(f"Data fetched successfully for company: {company_name}.")
            columns = [desc[0] for desc in cursor.description]
            return [dict(zip(columns, row)) for row in rows]                                                                                                                                
        else:
            print(f"No data found for company: {company_name}.")
            return None        
    
    except Exception as e:
        print(
            f"From DATABASE Service:\n"
            f"Error fetching data for {company_name}.\n"
            f"Error: {e}"
        )
        return None
    
    finally:
        if cursor:
            await cursor.close()
        if conn:
            await conn.close()
