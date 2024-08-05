from lib.db_connection import get_db_connection_with_database

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
