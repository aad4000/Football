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
        database=os.getenv("DB_NAME")
    )
    return connection

def drop_players_table():
    conn = get_db_connection_with_database()
    cursor = conn.cursor()
    
    cursor.execute("DROP TABLE IF EXISTS players")
    
    conn.commit()
    cursor.close()
    conn.close()

def create_players_table():
    conn = get_db_connection_with_database()
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS players (
        id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(100) NOT NULL,
        last_name VARCHAR(100) NOT NULL,
        apt INT NOT NULL,
        `set` INT NOT NULL,
        position ENUM('defender', 'midfielder', 'attacker') NOT NULL,
        national_association ENUM('England', 'Northern Ireland', 'Scotland', 'Wales') NOT NULL,
        avg FLOAT GENERATED ALWAYS AS ((apt + `set`) / 2) STORED
    )
    """)
    
    conn.commit()
    cursor.close()
    conn.close()
