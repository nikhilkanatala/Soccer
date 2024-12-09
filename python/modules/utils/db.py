'''
AzureDB Class
'''

import pyodbc
from modules.config import get_config

class AzureDBConn():
    """
    A class for handling connections to the database.
    """
    def __init__(self):
        self.connection = self.get_connection()
        self.cursor = self.get_cursor()
        
    def __enter__(self):
        self.connection = self.get_connection()
        self.cursor = self.get_cursor()
        return self    
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.connection.close()

    def get_connection(self):
        """
        Starts a new connection to the database.
        """
        config = get_config('azure-db')
        connection_string = f"DRIVER={config['driver']};SERVER=tcp:{config['server']};PORT=1433;DATABASE={config['database']};UID={config['username']};PWD={config['password']}" 
        conn = pyodbc.connect(connection_string)
        return conn

    def get_cursor(self):
        """
        Gets a cursor from the database connection.
        """
        return self.connection.cursor()
    
    def insert_dataframe_to_staging(self, df, table_name):
        """
        Insert a dataframe to a table in the database.
        """
        columns = ', '.join(df.columns)
        self.cursor.execute(f"TRUNCATE TABLE STAGING.{table_name}")
        query = f"INSERT INTO STAGING.{table_name} ({columns}) VALUES ({', '.join(['?']*len(df.columns))})"
        self.cursor.executemany(query, df.values.tolist())
        self.connection.commit()
        
        self.merge_staging_to_production(table_name)
        self.connection.commit()
        
    def merge_staging_to_production(self, table_name):
        """
        Merge the staging table to the production table.
        """
        self.cursor.execute(f"EXEC STAGING.MERGE_{table_name}")
        self.connection.commit()

    def executemany(self, query):
        """
        Execute a query and return the results.
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()    
    
    def finalize(self):
        """
        Closes the cursor and connection.
        """
        self.cursor.close()
        self.connection.close()
