import databases
import sqlalchemy

from core import config

engine = sqlalchemy.create_engine(config.DATABASE_URL)
metadata = sqlalchemy.MetaData()
database = databases.Database(config.DATABASE_URL)
