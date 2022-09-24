import logging

def api_log():
    logger = logging.getLogger('mylogger')
    logger.critical(f"{__name__} : helloworld")
