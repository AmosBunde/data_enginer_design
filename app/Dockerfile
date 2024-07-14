FROM python:3.9-slim

WORKDIR /app


RUN apt-get update && apt-get install -y python3-pip
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app




COPY ../scripts/run_docker.sh /app/run_docker.sh

RUN chmod +x /app/run_docker.sh

CMD ["/app/run_docker.sh"]
