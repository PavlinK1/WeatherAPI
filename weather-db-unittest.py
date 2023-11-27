import unittest
import sqlite3

class TestDatabaseOperations(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Connect to the existing database."""
        cls.conn = sqlite3.connect('weather_data.db')
        cls.cursor = cls.conn.cursor()

    @classmethod
    def tearDownClass(cls):
        """Close the database connection after all tests."""
        cls.conn.close()

    def test_insert_data(self):
        """Test inserting data into the table."""
        test_data = ('City', 25.0, 'Sunny', '1999-03-14 12:00:00')
        self.cursor.execute("INSERT INTO weather (city, temperature, description, timestamp) VALUES (?, ?, ?, ?);", test_data)
        self.conn.commit()
        self.cursor.execute("SELECT city, temperature, description, timestamp FROM weather WHERE city = 'City';")
        self.assertEqual(self.cursor.fetchone(), test_data)

    def test_retrieve_data(self):
        """Test retrieving data from the table."""
        self.cursor.execute("SELECT temperature FROM weather WHERE city = 'City';")
        self.assertEqual(self.cursor.fetchone()[0], 25.0)

    def test_delete_data(self):
        """Test deleting data from the table."""
        test_data = ('Town', 25.0, 'Sunny', '1999-03-14 12:00:00')
        self.cursor.execute("INSERT INTO weather (city, temperature, description, timestamp) VALUES (?, ?, ?, ?);", test_data)
        self.cursor.execute("DELETE FROM weather WHERE city = 'Town';")
        self.conn.commit()
        self.cursor.execute("SELECT * FROM weather WHERE city = 'Town';")
        self.assertIsNone(self.cursor.fetchone())

if __name__ == '__main__':
    unittest.main()


