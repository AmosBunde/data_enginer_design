#!/bin/bash

# Build the docker images
python /app/generate_and_insert_records.py

python /app/clickhouse_publisher.py

