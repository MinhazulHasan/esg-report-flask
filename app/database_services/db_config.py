from app.config.settings import config

DRIVER = config.DRIVER
SERVER_NAME = config.SERVER_NAME
DATABASE_NAME = config.DATABASE_NAME
TRUSTED_CONNECTION = config.TRUSTED_CONNECTION

# DSN-less connection string
CONNECTION_STRING = (
    f"DRIVER={{{DRIVER}}};"
    f"SERVER={SERVER_NAME};"
    f"DATABASE={DATABASE_NAME};"
    f"Trusted_Connection={TRUSTED_CONNECTION};"
)
