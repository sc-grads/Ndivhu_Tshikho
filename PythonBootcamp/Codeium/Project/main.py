import unittest
from connect_to_db import WordCounter

'''
class TestWordCounter(unittest.TestCase):

    def test_connect_to_db(self):
        counter = WordCounter()
        server = 'localhost'
        database = 'GraduateDB'
        username = 'User'
        password = 'Issa100@'
        connection = counter.connect_to_db(server, database, username, password)
        self.assertIsNotNone(connection)
        connection.close()


if __name__ == '__main__':
    unittest.main()

class TestWordCounter(unittest.TestCase):
    def test_connect_to_db(self):
        counter = WordCounter()
        server = 'localhost'
        database = 'GraduateDB'
        username = 'User'
        password = 'Issa100@'
        connection = counter.connect_to_db(server, database, username, password)
        self.assertIsNotNone(connection)
        connection.close()

    def test_read_from_CSV(self):
        file_path = 'example.csv'
        delimiter = ','
        quotechar = '"'
        encoding = 'utf-8'
        expected_rows = [[1, 'apple', 'red'], [2, 'banana', 'yellow']]
        rows = WordCounter.read_from_CSV(file_path, delimiter, quotechar, encoding)
        self.assertEqual(rows, expected_rows)


if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__'
'''



from counter import WordCounter

# Connect to a SQL Server database
counter = WordCounter()
server = 'localhost'
database = 'GraduateDB'
username = 'User'
password = 'Issa100@'
connection = counter.connect_to_db(server, database, username, password)

select_query = 'SELECT * FROM Timesheet'
cursor = connection.cursor()
cursor.execute(select_query)
rows = cursor.fetchall()

for row in rows:
    print(row)
connection.close()






