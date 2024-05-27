import sqlite3
import json


class DBHandler:

    def __init__(self, AlwaysInitializeDB:bool = False):
        """

        :param AlwaysInitializeDB: Only activate this when debugging Cupcake's database.
        """
        try:
            # Connect to your SQLite database
            self.conn = sqlite3.connect('Cupcake.sqlite3')
            self.curs = self.conn.cursor()

            if AlwaysInitializeDB:
                # Always call this function everytime new instances of this class created
                self.InitializeDB()
        except Exception as e:
            raise Exception(f"Error initializing database: {e}")

    def InitializeDB(self):
        """
        Used to initialize Cupcake's database.

        :return:
        """
        try:
            # Start a transaction
            self.curs.execute('BEGIN TRANSACTION')

            # Create table if it doesn't exist
            self.curs.execute('''
                CREATE TABLE IF NOT EXISTS "Server_Configs" (
                    "ServerID" TEXT NOT NULL UNIQUE,
                    "MessageConfigs" TEXT DEFAULT '{"Casual": {"WelcomeCID": "", "UserNotifCID": ""}, "Moderation:": {"ModLogsCID": ""}, "BotError": {"ErrorLogsCID": ""}}',
                    "PrivilegeConfigs" TEXT DEFAULT '{"Owner": "", "Admins": []}',
                    PRIMARY KEY("ServerID")
                )
            ''')
            self.curs.execute('''
                CREATE TABLE IF NOT EXISTS "Global_Blacklist" (
                    "UserID"	TEXT NOT NULL UNIQUE,
                    "RecordedProfileURL"	TEXT NOT NULL,
                    "RegisteredName"	TEXT DEFAULT 'No Recorded Name Provided',
                    "Reason"	TEXT DEFAULT 'No Recorded Reason Provided',
                    "BlacklistedBy"	TEXT NOT NULL,
                    "DateRegistered"	TEXT DEFAULT 'No Recorded Date Registered Provided',
                    PRIMARY KEY("UserID")
                )
            ''')
            self.curs.execute('''
                CREATE INDEX IF NOT EXISTS "Blacklisted_IDs" ON "Global_Blacklist" (
                    "UserID"
                )
            ''')
            self.curs.execute('''
                CREATE INDEX "RegisteredServer_IDs" ON "Server_Configs" (
                    "ServerID"
                )
            ''')

            # Commit the changes
            self.conn.commit()
        except Exception as e:
            # If an error occurred, rollback the transaction
            self.conn.rollback()
            raise Exception(f"Error initializing table: {e}")

    def RegisterServerConfigs(self, ServerID:str):
        """
        Used to register new entry of Server Configs to the database
        table named "Server_Configs" of Cupcake's Database.

        :param ServerID:
        :return:
        """

        try:
            # Insert a new server into the Server_Configs table
            self.curs.execute('''
                INSERT OR IGNORE INTO "Server_Configs" ("ServerID") VALUES (?)
            ''', (ServerID,))

            # Commit the changes
            self.conn.commit()
        except Exception as e:
            raise Exception(f"Error registering server: {e}")

    def ModifyServerConfigs(self, ServerID:str, Row:str, Key:str, NewValue:str):
        """
        Used to remove existing entry of Server Configs to the database
        table named "Server_Configs" of Cupcake's Database.

        :param ServerID:
        :param Row:
        :param Key:
        :param NewValue:
        :return:
        """

        try:
            # Fetch the current row value
            self.curs.execute('''
                        SELECT {} FROM "Server_Configs" WHERE "ServerID" = ?
                    '''.format(Row), (ServerID,))
            current_value = self.curs.fetchone()[0]

            # Parse the current value as JSON
            current_value_json = json.loads(current_value)

            # Modify the specific key in the JSON value
            current_value_json[Key] = NewValue

            # Convert the modified JSON back to a string
            new_value_str = json.dumps(current_value_json)

            # Update the row in the Server_Configs table
            self.curs.execute('''
                        UPDATE "Server_Configs" SET {} = ? WHERE "ServerID" = ?
                    '''.format(Row), (new_value_str, ServerID))

            # Commit the changes
            self.conn.commit()
        except Exception as e:
            raise Exception(f"Error modifying server configs: {e}")

    def RemoveServerConfigs(self, ServerID: str):
        """
        Used to remover existing entry of Server Configs to the database
        table named "Server_Configs" of Cupcake's Database.

        :param ServerID:
        :return:
        """

        try:
            # Remove a server from the Server_Configs table
            self.curs.execute('''
                DELETE FROM "Server_Configs" WHERE "ServerID" = ?
            ''', (ServerID,))

            # Commit the changes
            self.conn.commit()
        except Exception as e:
            raise Exception(f"Error removing server configs: {e}")
