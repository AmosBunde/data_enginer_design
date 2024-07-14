import psycopg2
from kafka import KafkaProducer,KafkaConsumer
import json
from clickhouse_driver import Client
import time

# PostgreSQL connection details
pg_conn = psycopg2.connect(
    dbname='irembo',
    user='amos',
    password='irembo24',
    host='postgres',  # 'postgres' as it's the service name in docker-compose
    port='5432'
)
pg_cursor = pg_conn.cursor()

# Kafka producer setup
producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# ClickHouse client setup
clickhouse_client = Client('clickhouse')

# Read data from PostgreSQL and push to Kafka
def push_to_kafka(table_name):
    pg_cursor.execute(f"SELECT * FROM {table_name}")
    rows = pg_cursor.fetchall()
    columns = [desc[0] for desc in pg_cursor.description]

    for row in rows:
        data = dict(zip(columns, row))
        producer.send(table_name, data)
    producer.flush()

# Read data from Kafka and push to ClickHouse
def consume_from_kafka_and_push_to_clickhouse(table_name):
    consumer = KafkaConsumer(
        table_name,
        bootstrap_servers='kafka:9092',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

    for message in consumer:
        data = message.value
        columns = ', '.join(data.keys())
        values = ', '.join(f"'{v}'" for v in data.values())
        clickhouse_client.execute(f"INSERT INTO {table_name} ({columns}) VALUES ({values})")

# Push data from PostgreSQL tables to Kafka
tables = ['Customer', 'Sales_Territory', 'Employee', 'Sales']
for table in tables:
    push_to_kafka(table)
    time.sleep(5)  # Give some time for Kafka to process the messages

# Consume data from Kafka and push to ClickHouse
for table in tables:
    consume_from_kafka_and_push_to_clickhouse(table)

pg_cursor.close()
pg_conn.close()