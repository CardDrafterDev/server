include .$(CURR_DIR)/.env

PORT=$(SERVER_PORT)
PYTHON=$(VENV)/bin/python3
HOST=$(SERVER_HOST)
CURR_DIR="D:\Programming\carddrafter\server"
# need to remake later ^

py-local:
	$(PYTHON) -m uvicorn 'main:app' --reload --host $(HOST) --port $(PORT)

uvi-local:
	uvicorn 'main:app' --reload --host $(HOST) --port $(PORT)

req:
	pip install -r requirements.txt
