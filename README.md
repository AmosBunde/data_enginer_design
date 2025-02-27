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
  
      
### Project Tree  
data\_enginer\_design/

├── .github/

│ └── workflows/

│ └── ci.yml

├── clickhouse-server-logs/

│ ├── clickhouse-server.err.log

│ └── clickhouse-server.log

├── app/

│ ├── Dockerfile

│ ├── clickhouse\_publisher.py

│ ├── generate\_and\_insert\_records.py

│ ├── requirements.txt

│ └── tests/

│ ├── datapublisher.py

│ └── test\_data\_generate.py

├── docker/

│ ├── Dockerfile.clickhouse

│ └── Dockerfile.postgres

├── docker-compose.yml

└── README.md

````
Data Engineering Architectural Workflows
````

![Diagram using Graphviz on CLI](https://github.com/user-attachments/assets/e363fdf8-81ef-45c4-b1fe-c87a32d819bd)

  
### Kafka Connect Configuration

Create a Kafka Connect configuration to capture changes from PostgreSQL and stream them to ClickHouse. This involves configuring Kafka Connect with the PostgreSQL source connector and ClickHouse sink connector.

### BI Dashboard

Configure Grafana to connect to ClickHouse and create dashboards for real-time reporting based on the data stored in ClickHouse.

### Summary

This setup will enable real-time data streaming from PostgreSQL to ClickHouse using Kafka, and visualizing the data in Grafana. This approach ensures low latency and real-time insights for Rembo Company’s business needs. The next steps involve implementing each component and ensuring they are correctly integrated to achieve the desired real-time reporting functionality.


### Disclaimer and Assumption
1. The solution is not complete.
2. The last git action on Postgres services start is main error that is still needs to be debugged.
3. I didn't initiate the Graphana/Apache Superset for Visualization because of point No. 2.
4. I picked the Conterized service for kafka because of:
       - It's easy to integrate with clickhouse drivers.
       - The CDC would be easily introduced to Kafka using Debezium of Table Primary Keys on the Topic.
5. I understand using Airflow container if feasible but not in the future needs such as CDC and Scalability of the same.(NB; I haven't explored using Kafka on Airflow but that would be another feasible solution.)
6. Check the git actions to gather my thought processes.
