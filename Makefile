PORT=8080
PYTHON=$(VENV)/bin/python3
HOST=127.0.0.1

py-local:
	$(PYTHON) -m uvicorn 'main:app' --reload --host $(HOST) --port $(PORT)

uvi-local:
	uvicorn 'main:app' --reload --host $(HOST) --port $(PORT)
