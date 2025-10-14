
"""


NOTE: I SUCK AT SQL AND HAVE NO ACCESS TO THE DATABASE.
I HAVE NO IDEA IF ANY OF THIS WORKS



"""
import mysql.connector
import os
from dotenv import load_dotenv
from mysql.connector import MySQLConnection
from typing import Optional, Tuple, Any, List

load_dotenv()


class SQLManager:
    """Manages database connections and queries"""
    
    def __init__(self):
        """Initialize SQLManager; doesn't connect immediately"""
        self.config = {
            "user": os.getenv("SQL_USER"),
            "password": os.getenv("SQL_PASSWORD"),
            "host": os.getenv("SQL_HOST"),
            "port": os.getenv("SQL_PORT"),
            "database": os.getenv("SQL_DATABASE")
        }
        print("SQLManager initialized")
    
    def _get_connection(self) -> MySQLConnection:
        """Establishes a new connection to the database"""
        try:
            cnx = mysql.connector.connect(**self.config)
            return cnx
        except mysql.connector.Error as err:
            print(f"Database connection error: {err}")
            raise
    
    def _execute_query(self, query: str, params: Tuple = None, fetch: str = None) -> Any:
        """Execute a query and handle connection lifecycle"""
        cnx = None
        cursor = None
        try:
            cnx = self._get_connection()
            cursor = cnx.cursor(buffered=True)
            cursor.execute(query, params or ())
            
            if fetch == "one":
                return cursor.fetchone()
            elif fetch == "all":
                return cursor.fetchall()
            else:
                cnx.commit()
                return None
                
        except mysql.connector.Error as err:
            print(f"Query execution error: {err}")
            if cnx:
                cnx.rollback()
            raise
        finally:
            if cursor:
                cursor.close()
            if cnx and cnx.is_connected():
                cnx.close()
    
    def update_user(self, user_id: int, username: str) -> None:
        query_check = "SELECT * FROM `users` WHERE `userID` = %s"
        result = self._execute_query(query_check, (user_id,), fetch="one")
        
        if result is None:
            # User doesn't exist, create them
            query_create = "INSERT INTO `users`(`userID`, `nickname`) VALUES (%s, %s);"
            self._execute_query(query_create, (user_id, username))
            print(f"Created new user: {username} (ID: {user_id})")
        else:
            # User exists, check if username changed
            if str(result[1]) != str(username):
                query_update = "UPDATE users SET nickname = %s WHERE userID = %s"
                self._execute_query(query_update, (username, user_id))
                print(f"Updated user: {username} (ID: {user_id})")
    
    def get_wallet(self, user_id: int) -> Tuple[bool, str]:
        """tf is a wallet?"""
        try:
            query = "SELECT * FROM `users` WHERE `userID` = %s"
            result = self._execute_query(query, (user_id,), fetch="one")
            
            if result:
                return (True, f"User wallet data: {result}")
            else:
                return (False, f"No wallet found for user ID: {user_id}")
        except Exception as e:
            return (False, f"Error fetching wallet: {str(e)}")
    
    def add_game_request(self, user_id: int, game: str, platform: str) -> Tuple[bool, str]:
        """Add a new game request to the database"""
        try:
            query = "INSERT INTO `game_request`(`userID`, `game`, `platform`) VALUES (%s, %s, %s);"
            self._execute_query(query, (user_id, game.lower().strip(), platform))
            return (True, f"Game request added: {game} on {platform}")
        except Exception as e:
            return (False, f"Error adding game request: {str(e)}")
    
    def get_game_requests(self) -> Tuple[bool, List]:
        """Retrieve all game requests from the database"""
        try:
            query = "SELECT * FROM `game_request`"
            results = self._execute_query(query, fetch="all")
            return (True, results or [])
        except Exception as e:
            return (False, str(e))
    
    def test_connection(self) -> bool:
        try:
            query = "SELECT 1"
            self._execute_query(query)
            print("Database connection test passed")
            return True
        except Exception as e:
            print(f"Database connection test failed: {e}")
            return False