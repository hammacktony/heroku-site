TEST_PATH=./tests/
MYPY_PATH=./

serve:
	gunicorn -w 4 -k uvicorn.workers.UvicornWorker app:app
dev:
	uvicorn app:app --reload
clean:
	find . -name '*.pyc' -delete
lint:
	flake8 --ignore=E501,F401,E128,E402,E731,F821,E712,W503
test: clean
	python3 -m pytest --verbose --color=yes $(TEST_PATH)
mypy:
	python3 -m mypy $(MYPY_PATH) --ignore-missing-imports --follow-imports=silent --show-column-numbers