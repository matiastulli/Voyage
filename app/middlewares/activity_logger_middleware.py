import json
from datetime import datetime
from flask import g, request
from loguru import logger
from app.controllers.database_controller import database_controller
from app.schemas.kpi import Log

def log_activity():
    logger.info("Log activity middleware")
    if g.current_user:
        
        session = database_controller.new_session()
        
        log = Log(
            user_email = g.current_user.mail,
            body_data = json.loads(request.data.decode('utf-8')),
            host = request.host,
            route = request.path,
            date = datetime.now()
        )

        session.add(log)
        session.commit()
        session.refresh(log)

        logger.info(f"User {log.user_email} accessed {log.route} at {log.date}")