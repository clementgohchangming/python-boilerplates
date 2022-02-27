import logging
from pythonjsonlogger import jsonlogger
from settings import LOGGING_LEVEL
from datetime import datetime


class CustomJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(CustomJsonFormatter, self).add_fields(log_record, record, message_dict)
        if not log_record.get('timestamp'):
            # this doesn't use record.created, so it is slightly off
            now = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
            log_record['timestamp'] = now
        if log_record.get('level'):
            log_record['level'] = log_record['level'].upper()
        else:
            log_record['level'] = record.levelname


logHandler = logging.StreamHandler()
formatter = CustomJsonFormatter()
logHandler.setFormatter(formatter)

# Singleton logger to be imported by other scripts
logger = logging.getLogger("your-service-name")
logger.propagate = False
logger.setLevel(LOGGING_LEVEL)
logger.addHandler(logHandler)
