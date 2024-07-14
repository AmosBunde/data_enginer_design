import unittest
import psycopg2
from clickhouse_driver import Client
import os

class TestPushDataToClickhouse(unittest.TestCase):

    def setUp(self):
        # PostgreSQL connection setup
        self.pg_conn = psycopg2.connect(
            host=os.getenv("POSTGRES_HOST", "localhost"),
            database=os.getenv("POSTGRES_DB", "rembo"),
            user=os.getenv("POSTGRES_USER", "user"),
            password=os.getenv("POSTGRES_PASSWORD", "password")
        )
        self.pg_cursor = self.pg_conn.cursor()

        # ClickHouse connection setup
        self.clickhouse_client = Client(host=os.getenv("CLICKHOUSE_HOST", "localhost"))

        # Ensure ClickHouse database exists
        self.clickhouse_client.execute('CREATE DATABASE IF NOT EXISTS rembo')

        # Create tables in ClickHouse
        self.clickhouse_client.execute('''
        CREATE TABLE IF NOT EXISTS rembo.Customer (
            Customer_Id Int32,
            Last_Name String,
            Address_Line1 String,
            Address_Line2 String,
            Birth_Date String,
            Age String,
            Commute_Distance String,
            Customer_Alternate_Key String,
            Customer_Key String,
            Date_First_Purchase String,
            Email_Address String,
            English_Education String,
            English_Occupation String,
            French_Education String,
            First_Name String,
            French_Occupation String,
            Gender String,
            House_Owner_Flag String,
            Marital_Status String,
            Middle_Name String,
            Name_Style String,
            Number_Cars_Owned String,
            Number_Children_At_Home String,
            Phone String,
            Spanish_Education String,
            Spanish_Occupation String,
            Suffix String,
            Title String,
            Total_Children String,
            Yearly_Income String
        ) ENGINE = MergeTree() ORDER BY Customer_Id
        ''')

    def tearDown(self):
        # Close PostgreSQL connection
        self.pg_cursor.close()
        self.pg_conn.close()

        # Drop the ClickHouse tables and database
        self.clickhouse_client.execute('DROP TABLE IF EXISTS rembo.Customer')
        self.clickhouse_client.execute('DROP DATABASE IF EXISTS rembo')

    def test_data_transfer(self):
        # Insert a test record into PostgreSQL
        self.pg_cursor.execute('''
        INSERT INTO Customer (Last_Name, Address_Line1, Birth_Date, Age, First_Name)
        VALUES ('Doe', '123 Main St', '2000-01-01', '23', 'John')
        ''')
        self.pg_conn.commit()

        # Run the data transfer script
        import clickhouse_publisher

        # Query ClickHouse to verify the data transfer
        result = self.clickhouse_client.execute('SELECT * FROM rembo.Customer WHERE Last_Name = \'Doe\'')
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][1], 'Doe')  # Last_Name
        self.assertEqual(result[0][2], '123 Main St')  # Address_Line1
        self.assertEqual(result[0][4], '2000-01-01')  # Birth_Date
        self.assertEqual(result[0][5], '23')  # Age
        self.assertEqual(result[0][13], 'John')  # First_Name

if __name__ == '__main__':
    unittest.main()