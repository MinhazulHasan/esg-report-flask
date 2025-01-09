from datetime import datetime, timezone
from app.utilities.logger import report_logger
from typing import Dict, List, Tuple
from app.database_services.db_utils import get_connection




def format_for_db(company_name: str, data_field: str, data: List[dict]) -> List[Tuple]:
    reported_at = datetime.now(timezone.utc)  # Use UTC for consistency.
    return [
        (
            company_name,
            data_field,
            entry["Year"],
            entry["Data"],
            reported_at
        )
        for entry in data
    ]


async def insert_or_update_company_report(company_name: str, data_field: str, data: List[dict]) -> None:
    formatted_data = format_for_db(company_name, data_field, data)
    conn = await get_connection()
    cursor = await conn.cursor()

    try:
        for record in formatted_data:
            company_name, data_field, year, response, reported_at = record

            # Check if the record exists
            await cursor.execute(
                """
                SELECT COUNT(1)
                FROM ESGReport
                WHERE company_name = ? AND data_field = ? AND year = ?
                """,
                (company_name, data_field, year),
            )
            exists = await cursor.fetchone()

            if exists and exists[0] > 0:
                # Update the existing record
                await cursor.execute(
                    """
                    UPDATE ESGReport
                    SET response = ?, reported_at = ?
                    WHERE company_name = ? AND data_field = ? AND year = ?
                    """,
                    (response, reported_at, company_name, data_field, year),
                )
                report_logger.info(f"From DATABASE Service: Data updated successfully for {company_name}, field: {data_field}.")
            
            else:
                # Insert new record
                await cursor.execute(
                    """
                    INSERT INTO ESGReport (company_name, data_field, year, response, reported_at)
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (company_name, data_field, year, response, reported_at),
                )
                report_logger.info(f"From DATABASE Service: Data inserted successfully for {company_name}, field: {data_field}.")
        
        await conn.commit()

    except Exception as e:
        report_logger.error(
            f"From DATABASE Service:\n"
            f"Error inserting data for company: {company_name}, field: {data_field}, "
            f"data: {formatted_data}, error: {str(e)}",
            exc_info=True
        )
        await conn.rollback()  # Rollback the transaction on failure.
        raise RuntimeError("Failed to insert data into ESGReport.") from e
    
    finally:
        await cursor.close()
        await conn.close()



async def insert_company_report_table_without_year(company_name: str, data_field: str, response: str) -> None:
    reported_at = datetime.now()

    # Establish a database connection
    conn = await get_connection()
    cursor = await conn.cursor()

    try:
        # Check if the record exists
        await cursor.execute(
            """
            SELECT COUNT(1)
            FROM ESGReport
            WHERE company_name = ? AND data_field = ?
            """,
            (company_name, data_field),
        )
        exists = await cursor.fetchone()

        if exists and exists[0] > 0:
            # Update the existing record
            await cursor.execute(
                """
                UPDATE ESGReport
                SET response = ?, reported_at = ?
                WHERE company_name = ? AND data_field = ?
                """,
                (response, reported_at, company_name, data_field),
            )
            report_logger.info(f"Data updated successfully for {company_name}, field: {data_field}.")

        else:
            # Insert new record
            await cursor.execute(
                """
                INSERT INTO ESGReport (company_name, data_field, response, reported_at)
                VALUES (?, ?, ?, ?)
                """,
                (company_name, data_field, response, reported_at),
            )
            report_logger.info(f"Data inserted successfully for {company_name}, field: {data_field}.")

        await conn.commit()

    except Exception as e:
        report_logger.error(
            f"Error inserting data for company: {company_name}, field: {data_field}, "
            f"response: {response}, error: {str(e)}",
            exc_info=True
        )
        await conn.rollback()  # Rollback the transaction on failure.
        raise RuntimeError("Failed to insert data into ESGReport.") from e

    finally:
        await cursor.close()
        await conn.close()