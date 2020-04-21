from settings.settings import POSTGRESQL
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(POSTGRESQL, connect_args={'connect_timeout': 10})
Session = sessionmaker(bind=engine)
metadata = MetaData()
Base = declarative_base(metadata=metadata)


class Database:
    def __enter__(self):
        self.session = Session()
        return self.session

    def __exit__(self, type, value, traceback):
        self.session.close()
