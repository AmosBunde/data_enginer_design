# Data Engineering Infrastructure

````
Data Engineering Systems Design
````
### System Design Flow

1.  **Source Database (PostgreSQL)**:
    
    *   Store the schema and initial data in a PostgreSQL database.
        
2.  **Message Broker (Kafka)**:
    
    *   Capture changes from PostgreSQL and publish them to Kafka topics.
        
3.  **Data Warehouse (ClickHouse)**:
    
    *   Consume messages from Kafka and load them into ClickHouse for OLAP queries.
        
4.  **Dashboard**:
    
    *   Use a BI tool (e.g., Grafana) to visualize the data in ClickHouse in real-time.
        

### Implementation Steps

1.  **Set Up PostgreSQL with Docker**:Create a Docker container for PostgreSQL and load the provided schema.
    
2.  **Set Up Kafka with Docker**:Create a Docker container for Kafka to handle data streaming.
    
3.  **Set Up ClickHouse with Docker**:Create a Docker container for ClickHouse to act as the OLAP database.
    
4.  **Data Pipeline**:
    
    *   Use Kafka Connect to capture changes from PostgreSQL.
        
    *   Set up Kafka Connect ClickHouse sink to load data into ClickHouse.
        
5.  **Dashboard**:
    
    *   Set up Grafana to visualize the data from ClickHouse.

