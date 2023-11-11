import os
from loguru import logger
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import SQLAlchemyError

load_dotenv()

class DatabaseController:
    def __init__(self) -> None:
        self.engine = create_engine(os.environ.get("ENV_SQLSERVER_VOYAGE"),
                                    pool_size=10,
                                    max_overflow=20)

    def get_session(self) -> Session:
        SessionLocal = sessionmaker(bind=self.engine)
        return SessionLocal()

    class DatabaseSession:
        def __init__(self, controller) -> None:
            self.controller = controller
            self.session = None

        def __enter__(self) -> Session:
            self.session = self.controller.get_session()
            return self.session

        def __exit__(self, exc_type, exc_val, exc_tb):
            try:
                if exc_type is None:
                    self.session.commit()
                else:
                    self.session.rollback()
            except SQLAlchemyError as exception:
                logger.error(exception)
            except Exception as exception:
                logger.error(exception)
            finally:
                self.session.close()

database_controller = DatabaseController()
