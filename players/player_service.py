from lib.db_connection import get_db_connection_with_database
import random

def insert_player(first_name, last_name, apt, set, position, national_association):
    conn = get_db_connection_with_database()
    cursor = conn.cursor()
    
    query = """
    INSERT INTO players (first_name, last_name, apt, `set`, position, national_association)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    
    cursor.execute(query, (first_name, last_name, apt, set, position, national_association))
    conn.commit()
    
    cursor.close()
    conn.close()

def insert_sample_data():
    conn = get_db_connection_with_database()
    cursor = conn.cursor()
    
    sample_data = [
        ('Harry', 'Kane', 85, 90, 'attacker', 'England'),
        ('Gareth', 'Bale', 88, 87, 'attacker', 'Wales'),
        ('Steven', 'Davis', 80, 78, 'midfielder', 'Northern Ireland'),
        ('Andy', 'Robertson', 84, 83, 'defender', 'Scotland'),
        # Add more sample data as needed
    ]
    
    query = """
    INSERT INTO players (first_name, last_name, apt, `set`, position, national_association)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    
    cursor.executemany(query, sample_data)
    conn.commit()
    
    cursor.close()
    conn.close()

def select_team(num_players):
    conn = get_db_connection_with_database()
    cursor = conn.cursor()
    
    query = """
    SELECT * FROM players
    ORDER BY `set` DESC
    """
    
    cursor.execute(query)
    players = cursor.fetchall()
    random_players = random.sample(players, num_players)
    
    cursor.close()
    conn.close()
    
    return random_players

def count_players_by_position():
    conn = get_db_connection_with_database()
    cursor = conn.cursor()
    
    query = """
    SELECT position, COUNT(*) as count FROM players GROUP BY position
    """
    
    cursor.execute(query)
    count_by_position = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return count_by_position

def get_all_players_sorted_by_apt():
    conn = get_db_connection_with_database()
    cursor = conn.cursor()
    
    query = """
    SELECT * FROM players ORDER BY apt DESC
    """
    
    cursor.execute(query)
    sorted_players = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return sorted_players

def get_player_with_highest_apt():
    conn = get_db_connection_with_database()
    cursor = conn.cursor()
    
    query = """
    SELECT * FROM players ORDER BY apt DESC LIMIT 1
    """
    
    cursor.execute(query)
    highest_apt_player = cursor.fetchone()
    
    cursor.close()
    conn.close()
    
    return highest_apt_player

def get_player_with_lowest_avg():
    conn = get_db_connection_with_database()
    cursor = conn.cursor()
    
    query = """
    SELECT * FROM players ORDER BY avg ASC LIMIT 1
    """
    
    cursor.execute(query)
    lowest_avg_player = cursor.fetchone()
    
    cursor.close()
    conn.close()
    
    return lowest_avg_player

def verify_table_schema():
    conn = get_db_connection_with_database()
    cursor = conn.cursor()
    
    cursor.execute("DESCRIBE players")
    schema = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    for column in schema:
        print(column)
