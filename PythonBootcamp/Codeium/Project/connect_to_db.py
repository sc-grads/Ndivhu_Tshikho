import pyodbc

class WordCounter:
    def connect_to_db(self, server, database, username, password):
        """
        Connect to a SQL Server database.

        Args:
            server (str): The name or IP address of the server.
            database (str): The name of the database.
            username (str): The username to use for the connection.
            password (str): The password to use for the connection.

        Returns:
            pyodbc.Connection: A connection to the database.
        """
        conn_str = 'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={};DATABASE={};UID={};PWD={}'
        conn_str = conn_str.format(server, database, username, password)
        return pyodbc.connect(conn_str)

def read_from_CSV(file_path, delimiter=',', quotechar='"', encoding='utf-8'):
        """
        Reads a CSV file at the specified path.

        Args:
            file_path (str): The path of the CSV file to read.
            delimiter (str): The character that separates values in the CSV file. Default is ','.
            quotechar (str): The character used to quote CSV fields. Default is '"'.
            encoding (str): The encoding of the CSV file. Default is 'utf-8'.

        Returns:
            list: The rows of the CSV file as a list of lists.
        """
        with open(file_path, 'r', encoding=encoding) as file:
            reader = csv.reader(file, delimiter=delimiter, quotechar=quotechar)
            return list(reader)


