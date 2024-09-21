install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black *.py

lint:
	pylint --disable=R,C library.py

test:
	python -m pytest -vv --cov=library --cov=main test_*.py

all: install lint test