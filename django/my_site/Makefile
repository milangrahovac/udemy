stop:
	sh stop_server.sh

run: stop
	sleep 1
	python3 manage.py runserver

create_reqirements:
	pip3 freeze > requirements.txt

install_reqirements:
	pip3 install -r requirements.txt

migrate:
	python3 manage.py makemigrations
	sleep 1
	python3 manage.py migrate
