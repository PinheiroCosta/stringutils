.PHONY: build build-dev run run-dev stop-dev lint typecheck test shell

build:
	docker build --target prod -t stringutils . --no-cache

build-dev:
	docker build --target dev -t stringutils-dev . --no-cache

run:
	docker run --rm -p 5010:5010 -e PORT=5010 stringutils

run-dev:
	docker run --rm -d \
	--name stringutils-dev \
	-p 5010:5010 \
	-e PORT=5010 \
	-v $(PWD):/app \
	-w /app \
	stringutils-dev \
	poetry run uvicorn app.main:app --host 0.0.0.0 --port 5010 --reload
	docker network connect romweb_dev_network stringutils-dev

stop-dev:
	docker stop stringutils-dev

lint:
	docker run --rm -v $(PWD):/app -w /app stringutils-dev poetry run flake8 -v app tests

typecheck:
	docker run --rm -v $(PWD):/app -w /app stringutils-dev poetry run mypy .

test:
	docker run --rm -v $(PWD):/app -w /app stringutils-dev poetry run env PYTHONPATH=/app pytest tests

shell:
	docker run --rm -it -v $(PWD):/app -w /app stringutils-dev /bin/sh

lock:
	docker run --rm -v $(PWD):/app -w /app stringutils-dev poetry lock
