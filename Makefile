.PHONY: build build-dev run run-dev lint typecheck test shell

build:
	docker build --target prod -t stringutils .

build-dev:
	docker build --target dev -t stringutils-dev .

run:
	docker run --rm -p 5010:5010 -e PORT=5010 stringutils

run-dev:
	docker run --rm -it -p 5010:5010 -e PORT=5010 -v $(PWD):/app -w /app stringutils-dev /bin/sh

lint:
	docker run --rm -v $(PWD):/app -w /app stringutils-dev flake8 -v app tests

typecheck:
	docker run --rm -v $(PWD):/app -w /app stringutils-dev mypy .

test:
	docker run --rm -v $(PWD):/app -w /app stringutils-dev pytest tests

shell:
	docker run --rm -it -v $(PWD):/app -w /app stringutils-dev /bin/sh

