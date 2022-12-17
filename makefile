install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	yapf -ir -vv --style pep8 .
lint:
	touch app/__init__.py
	pylint app --verbose --disable=R,C -sy
	rm app/__init__.py
test:
	docker-compose up -d
	sleep 5
	docker exec -t backend python3 -m pytest
	docker-compose stop
	docker rm -f db
	docker volume rm postgres_data
all: install format lint test 
