FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


COPY generate_and_insert_records.py generate_and_insert_records.py
COPY clickhouse_publisher.py   clickhouse_publisher.py
COPY appentry.sh appentry.sh

CMD ["sh", "appentry.sh"]
