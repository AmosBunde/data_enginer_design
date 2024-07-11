import psycopg2
import pytest

# PostgreSQL connection details

@pytest.fixture
def db_connection():
    conn = psycopg2.connect(
    dbname='irembo',
    user='amos',
    password='irembo24',
    host= 'postgres_test',
    port='5433'
)
    yield conn
    conn.close()


def test_customer_table(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM Customer")
    count = cursor.fetchone()[0]
    assert count > 0

def test_employee_table(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM Employee")
    count = cursor.fetchone()[0]
    assert count > 0

def test_sales_table(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM Sales")
    count = cursor.fetchone()[0]
    assert count > 0