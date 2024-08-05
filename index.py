import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from players.player_schema import drop_players_table, create_players_table
from players.player_service import insert_sample_data, verify_table_schema
from players.routes import create_app
from lib.db_connection import create_database

if __name__ == "__main__":
    create_database()  # Ensure the database is created
    drop_players_table()
    create_players_table()
    verify_table_schema()  # Verify the table schema before inserting data
    insert_sample_data()
    verify_table_schema()  # Verify the table schema after inserting data
    app = create_app()
    app.run(debug=True)
