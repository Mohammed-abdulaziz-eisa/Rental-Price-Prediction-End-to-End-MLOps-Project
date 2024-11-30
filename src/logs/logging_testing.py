# DUBUG -> function parameters level
# INFO -> running order of application
# WARNING -> it's ok but needs your attention
# ERROR -> error in part of your application
# CRITICAL -> critical error in your application (db connection - db not found)
# TRACE ->  log everything in your application

from loguru import logger

# create a logger object
logger.add("app.log")
