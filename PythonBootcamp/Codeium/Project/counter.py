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


'''
   def count_words(self, sentence):
        """
        Count the number of words in a sentence.

        Args:
            sentence (str): The sentence to count the words in.

        Returns:
            int: The number of words in the sentence.
        """
        words = sentence.split(' ')
        count = sum(1 for word in words if word)
        return count


    def count_unique_words(self, sentence):
        """
        Count the number of unique words in a sentence.


'''
 