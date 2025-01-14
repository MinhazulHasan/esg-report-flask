from app.database_services.db_utils import get_connection


async def create_esg_report_table():
    conn = await get_connection()
    try:
        cursor = await conn.cursor()
        create_table_sql = """
            IF NOT EXISTS (
                SELECT 1 
                FROM sys.objects 
                WHERE object_id = OBJECT_ID(N'[dbo].[ESGReport]') 
                  AND type = N'U'
            )
            BEGIN
                CREATE TABLE ESGReport (
                    id INT IDENTITY(1,1) PRIMARY KEY,
                    company_name VARCHAR(255),
                    data_field VARCHAR(255),
                    year VARCHAR(10),
                    response TEXT,
                    reported_at DATETIME DEFAULT GETDATE()
                )
            END;
        """
        await cursor.execute(create_table_sql)
        await conn.commit()
    except Exception as e:
        raise
    finally:
        await cursor.close()
        await conn.close()
        