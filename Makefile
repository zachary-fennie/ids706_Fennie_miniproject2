install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black *.py

lint:
	pylint --disable=R,C funcs.py

test:
	python -m pytest -vv --cov=hello test_main.py

generate and push:
	python main.py
	git config # email
	git config # username
	git add .
	git commit -m "test"
	git push

all: install lint test