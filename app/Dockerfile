FROM python:3.9-slim

WORKDIR /app/



RUN pip install -r requirements.txt

COPY . /app



COPY ../scripts/run_docker.sh /app/run_docker.sh

RUN chmod +x /app/run_docker.sh

CMD ["/app/run_docker.sh"]
