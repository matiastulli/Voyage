import json
from datetime import datetime
from flask import g, request
from loguru import logger
from app.controllers.database_controller import database_controller
from app.schemas.kpi import Log

def log_activity():
    logger.info("Log activity middleware")
    if g.current_user:
        try:
            body_data = json.loads(request.data.decode('utf-8'))
        except json.JSONDecodeError as e:
            logger.error(f"Error decoding JSON: {e}")
            body_data = None

        with database_controller.DatabaseSession(database_controller) as session:
            log = Log(
                user_mail=g.current_user["mail"],
                body_data=body_data,
                host=request.host,
                route=request.path,
                date=datetime.now()
            )

            session.add(log)
            session.flush()

            logger.info(f"User {log.user_mail} accessed {log.route} at {log.date}")
