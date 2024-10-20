.PHONY: source clean

stop_server:
	sh stop_server.sh

run_server: stop_server
	sleep 1
	python3 manage.py runserver

create_reqirements:
	pip3 freeze > requirements.txt

install_reqirements:
	pip3 install -r requirements.txt

activate_env:
	source ./venv/bin/activate   

stop_env:
	deactivate

clean:
	rm -rf __pycache__
	rm -rf venv

VENV_DIR = venv

run: 
	$(VENV_DIR)/bin/python3 manage.py runserver

migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate
