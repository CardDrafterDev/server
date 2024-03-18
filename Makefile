include $(PWD)/.env

PORT=$(SERVER_PORT)
PYTHON=$(VENV)/bin/python3
HOST=$(SERVER_HOST)


py-local:
	$(PYTHON) -m uvicorn 'main:app' --reload --host $(HOST) --port $(PORT)

uvi-local:
	uvicorn 'main:app' --reload --host $(HOST) --port $(PORT)

req:
	pip install -r requirements.txt
