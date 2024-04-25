include $(PWD)/.env

PORT=$(SERVER_PORT)
PYTHON=$(VENV)/bin/python3
HOST=$(SERVER_HOST)


py-local:
	$(PYTHON) -m uvicorn 'main:server' --reload --host $(HOST) --port $(PORT)

uvi-local:
	uvicorn 'main:server' --reload --host $(HOST) --port $(PORT)

req-make:
	$(PYTHON) -m pipreqs.pipreqs ./ --force

req:
	pip install -r requirements.txt
	pip install uvicorn==0.15.0


check-redis:
	(printf "PING\r\n";) | nc $(REDIS_HOST) $(REDIS_PORT)
