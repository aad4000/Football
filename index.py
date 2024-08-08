import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from players.player_service import insert_sample_data, verify_table_schema 
from players.routes import create_app
from lib.db_connection import create_database, create_players_table, drop_players_table

if __name__ == "__main__":
    create_database() 
    drop_players_table() 
    create_players_table()
    verify_table_schema()  
    insert_sample_data()
    verify_table_schema()
    
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
