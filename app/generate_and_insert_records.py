import psycopg2
from psycopyg2.extras import execute_values
from faker import Faker
import random

# PostgreSQL connection details

conn = psycopg2.connect(
    dbname='irembo',
    user='amos',
    password='irembo24',
    host= 'postgres',
    port='5432'
)

cursor = conn.cursor()

#Initialize Faker Data

data = Faker()

# Generate and insert customers
def CustomerData(cursor, num_customers=500000):
    customers = []
    for _ in range(num_customers):
        customers.append((
            data.last_name(), data.street_address(), data.secondary_address(),
            data.date_of_birth().strftime('%Y-%m-%d'), str(random.randint(18, 90)), data.random_number(digits=2),
            data.random_number(digits=6), data.random_number(digits=6),
            data.date_this_decade().strftime('%Y-%m-%d'), data.email(), data.job(), data.job(), data.job(),
            data.first_name(), data.job(), data.random_element(elements=('M', 'F')), data.random_element(elements=('Y', 'N')),
            data.random_element(elements=('Single', 'Married')), data.first_name(), data.random_element(elements=('M', 'F')),
            str(random.randint(0, 5)), str(random.randint(0, 5)), data.phone_number(), data.job(), data.job(),
            data.suffix(), data.prefix(), str(random.randint(0, 5)), str(random.randint(20000, 200000))
        ))

        if len(customers) % 10000 == 0:
            insert_query = """
            INSERT INTO Customer (
                Last_Name, Address_Line1, Address_Line2, Birth_Date, Age, Commute_Distance, 
                Customer_Alternate_Key, Customer_Key, Date_First_Purchase, Email_Address, 
                English_Education, English_Occupation, French_Education, First_Name, 
                French_Occupation, Gender, House_Owner_Flag, Marital_Status, Middle_Name, 
                Name_Style, Number_Cars_Owned, Number_Children_At_Home, Phone, 
                Spanish_Education, Spanish_Occupation, Suffix, Title, Total_Children, 
                Yearly_Income
            ) VALUES %s
            """
            execute_values(cursor, insert_query, customers)
            customers = []

    if customers:
        execute_values(cursor, insert_query, customers)

    conn.commit()

def InsertSalesTerritories(cursor, num_territories=11):
    territories = []
    for _ in range(num_territories):
        territories.append((
            data.country(), data.state(), data.city()
        ))

    insert_query = """
    INSERT INTO Sales_Territory (
        Sales_Territory_Country, Sales_Territory_Region, Sales_Territory_City
    ) VALUES %s
    """
    execute_values(cursor, insert_query, territories)
    conn.commit()

# Generate and insert employees
def EmployeeData(cursor, num_employees=1000):
    employees = [(data.name(), data.state()) for _ in range(num_employees)]
    insert_query = """
    INSERT INTO Employee (Employee_Name, Employee_Territory_Region)
    VALUES %s
    """
    execute_values(cursor, insert_query, employees)
    conn.commit()

# Generate and insert sales
def SalesData(cursor, num_sales=250000000, batch_size=100000):
    sales = []
    for _ in range(num_sales):
        sales.append((
            data.currency_code(), data.random_number(digits=6), 
            str(random.uniform(0, 500)), data.date_this_year().strftime('%Y-%m-%d'), data.random_number(digits=8),
            str(random.uniform(10, 1000)), str(random.uniform(5, 100)), data.date_this_year().strftime('%Y-%m-%d'), 
            str(random.randint(1, 10)), str(random.uniform(10, 100)), data.random_number(digits=1),
            str(random.uniform(10, 2000)), str(random.randint(1, 100)), data.random_number(digits=6),
            data.date_this_year().strftime('%Y-%m-%d'), str(random.uniform(10, 200)), str(random.uniform(5, 100)),
            data.random_element(elements=('F', 'M')), str(random.randint(1, 100))
        ))

        if len(sales) % batch_size == 0:
            insert_query = """
            INSERT INTO Sales (
                CurrencyKey, CustomerKey, Discount_Amount, DueDate, DueDateKey, Extended_Amount, 
                Freight, Order_Date, Order_Quantity, Product_Standard_Cost, Revision_Number, 
                Sales_Amount, Sales_Order_Line_Number, Sales_Order_Number, SalesTerritoryKey, 
                ShipDate, Tax_Amt, Total_Product_Cost, Unit_Price, Unit_Price_Discount_Pct, 
                Employee_Id
            ) VALUES %s
            """
            execute_values(cursor, insert_query, sales)
            sales = []

    if sales:
        execute_values(cursor, insert_query, sales)

    conn.commit()

# Run the data generation and insertion
CustomerData(cursor)
InsertSalesTerritories(cursor)
EmployeeData(cursor)
SalesData(cursor)

cursor.close()
conn.close()
