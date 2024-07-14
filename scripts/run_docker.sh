#!/bin/bash

# Wait for PostgreSQL to be ready
while ! docker-compose exec postgres psql -h postgres -U amos -l &> /dev/null; do
  sleep 1
done

# Wait for Kafka to be ready
while ! docker-compose logs kafka 2>&1 | grep -q 'started'; do
  sleep 1
done

# Wait for ClickHouse to be ready
while ! docker-compose logs clickhouse 2>&1 | grep -q 'started'; do
  sleep 1
done

# Build the docker images
python /app/generate_and_insert_records.py

python /app/clickhouse_publisher.py

