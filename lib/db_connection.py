import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )
    return connection

def create_database():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS football")
    cursor.close()
    connection.close()

def get_db_connection_with_database():
    create_database()
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database='football'
    )
    return connection
