.PHONY: build up down clean logs test

build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

clean:
	docker-compose down -v --rmi all

logs:
	docker-compose logs -f

test:
	docker-compose -f docker-compose.test.yml up --abort-on-container-exit --build

	