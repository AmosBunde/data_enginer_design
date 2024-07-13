#!/bin/bash

# Build the docker images
docker-compose build

# Start the services
docker-compose up -d

# Wait for PostgreSQL to be ready
while ! docker-compose exec postgres pg_isready -U user; do
  echo "Waiting for PostgreSQL to be ready..."
  sleep 2
done

# Run the faker_generate_data.py script to populate the PostgreSQL database
docker-compose exec app python generate_and_insert_records.py

echo "Docker containers are up and running!"