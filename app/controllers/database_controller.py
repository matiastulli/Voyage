import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

class DatabaseController():
    def __init__(self) -> None:
        self.engine = create_engine(os.environ.get("ENV_SQLSERVER_VOYAGE"),
                                    pool_size=10,
                                    max_overflow=20)
    def new_session(self):
        return sessionmaker(bind=self.engine)()

database_controller = DatabaseController()