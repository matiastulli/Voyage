from flask import request
from app.libs.database import database
from app.schemas.kpi import Log

class LoggerController():
    
    def create_log(self, log: dict):
        data = request.json
        session = database.new_session()
        
        log = Log(
            user_email = data["user_email"],
            body_data = data["body_data"],
            host = data["host"],
            route = data["route"],
            date = data["date"]
        )

        session.add(log)
        session.commit()
        session.refresh(log)
        
        return log

logger_controller = LoggerController()
