from sqlalchemy import create_engine, MetaData
from databases import Database

# Define the database URL for PostgreSQL
DATABASE_URL = "postgresql://user:password@db:5432/ecommerce_db"

# Initialize the Database object
database = Database(DATABASE_URL)

# Initialize the MetaData object for table definitions
metadata = MetaData()
