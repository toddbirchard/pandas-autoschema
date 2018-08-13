import psycopg2
from config import database, host, user, password
import logging

# Enabled logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Set conn as global var
conn = None


def openConnection():
    """Database connection handler."""
    global conn
    try:
        if(conn is None):
            conn = psycopg2.connect(host=host, database=database, user=user, password=password)
        elif (not conn.open):
            conn = psycopg2.connect(host=host, database=database, user=user, password=password)
    except Exception as e:
        print("Can't connect. You failed. Game over.")
        print(e)


logger.info("SUCCESS: time to steal data.")
