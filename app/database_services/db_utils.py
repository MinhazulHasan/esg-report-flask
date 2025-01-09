import aioodbc
from app.utilities.logger import report_logger
from app.database_services.db_config import CONNECTION_STRING

async def get_connection() -> aioodbc.Connection:
    try:
        return await aioodbc.connect(dsn=CONNECTION_STRING)
    except Exception as e:
        report_logger.error(f"Error establishing database connection: {str(e)}", exc_info=True)
        raise RuntimeError("Failed to establish a database connection. Please check your configuration.") from e
