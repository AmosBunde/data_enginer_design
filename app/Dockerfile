FROM python:3.9-slim

WORKDIR /app


RUN apt-get update && apt-get install -y python3-pip
RUN pip install --upgrade pip
RUN pip install clickhouse-driver==0.2.8
RUN pip install Faker==26.0.0
RUN pip install iniconfig==2.0.0
RUN pip install kafka==1.3.5
RUN pip install packaging==24.1
RUN pip install pluggy==1.5.0
RUN pip install psycopg2-binary==2.9.9
RUN pip install pytest==8.2.2
RUN pip install python-dateutil==2.9.0.post0
RUN pip install pytz==2024.1
RUN pip install six==1.16.0
RUN pip install tzlocal==5.2
##RUN pip install -r requirements.txt

COPY . /app




COPY ../scripts/run_docker.sh /app/run_docker.sh

RUN chmod +x /app/run_docker.sh

CMD ["/app/run_docker.sh"]
