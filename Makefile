.PHONY: default
default:
	pip3 install -r requirements.txt
	git submodule init
	git submodule update
	python3 manage.py makemigrations
	python3 manage.py migrate

.PHONY: clean
clean:
	find . -type d -name __pycache__ -exec rm -r {} \+

.PHONY: run
run:
	python3 manage.py runserver
