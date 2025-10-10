"""This module acts as the connection between the bot and the SQL management folder. Everything outside the directory
should only interact with this module"""
import interactions
import mysql.connector

import os
from dotenv import load_dotenv

from mysql.connector import MySQLConnection

from interactions import User
from typing_extensions import deprecated

load_dotenv()  # Loads the .env file


class SQLManager:
    # cnx: MySQLConnection  # The connection used to connect to the database

    # TODO: Keeping the connection open the entire time wastes resources, and doesn't work seeing as the connection
    # TODO:     closes itself anyways. Instead, just have a method or class that opens a connection whenever we need it.

    def __init__(self):
        # self._connection = SQLConnection()
        print("Establishing connection to NWMSU Gaming database...")

        return  # don't connect (DEBUG)

        self.cnx = mysql.connector.connect(user=os.getenv("SQL_USER"), password=os.getenv("SQL_PASSWORD"),
                                           host=os.getenv("SQL_HOST"), port=os.getenv("SQL_PORT"),
                                           database=os.getenv("SQL_DATABASE"))
        self.cursor = self.cnx.cursor(buffered=True)  # This is used to interact with the actual database
        print("Connection Verified.\n\n")

        disconnect()


    def connect(self) -> None:
        """
        Establishes a connection to the database
        :return: None
        """
        self.cnx = mysql.connector.connect(user=os.getenv("SQL_USER"), password=os.getenv("SQL_PASSWORD"),
                                           host=os.getenv("SQL_HOST"), port=os.getenv("SQL_PORT"),
                                           database=os.getenv("SQL_DATABASE"))
        self.cursor = self.cnx.cursor(buffered=True)  # This is used to interact with the actual database
        print("Connection Established.\n\n")


    def disconnect(self) -> None:
        """
        Closes the connection to the database
        :return: None
        """

        print("Closing DB Connection")
        self.cursor.close()
        self.cnx.close()
        print("DB Connection Closed")

    def is_closed(self) -> bool:
        return self.cnx.is_connected()

    #@deprecated
    def updateUser(self, user: User):
        """
        Checks to see if a user has been added to the database yet.
        :param user: user to check
        :return: True if they exist, false otherwise
        """
        query_userTable = "SELECT * FROM `users` WHERE `userID` = %s"
        self.cursor.execute(query_userTable, (int(user.id),))

        result = self.cursor.fetchone()

        if result is None:
            query_createUser = "INSERT INTO `users`(`userID`, `nickname`) VALUES (%s,%s);"
            self.cursor.execute(query_createUser, (int(user.id), str(user.username)))
            # Default in the hard database will handle favors, no need to pass it in here
            self.cnx.commit()
        else:
            if str(result[1]) == str(user.username):
                return
            query_updateUser = "UPDATE users SET nickname = %s WHERE userID = %s"
            self.cursor.execute(query_updateUser, (str(user.username), str(user.id)))
            self.cnx.commit()

    def test_connection(self):
        query = "SELECT * FROM `game_request` WHERE 1"

        self.connect()

        self.cursor.execute(query)
        result = self.cursor.fetchall()
        print(result)

        self.disconnect()


    def close(self):
        """Closes the connection"""

        print("Closing Connection")
        self.cursor.close()
        self.cnx.close()
        print("Connection Closed")
