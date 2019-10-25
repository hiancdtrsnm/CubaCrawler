.PHONY: build clean install test lint cov

# TODO: Update your project folder
PROJECT=CubaCrawler

build:
	pipenv run python setup.py sdist bdist_wheel

clean:
	git clean -fxd

install:
	pip install pipenv
	pipenv install --dev --skip-lock

test:
	make lint && pipenv run pytest --doctest-modules --cov=$(PROJECT) --cov-report=xml -v

lint:
	pipenv run pylint $(PROJECT) || pipenv run pylint-exit $$?

cov:
	pipenv run codecov
