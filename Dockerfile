# Stage 1: Build dev com dependências dev (mypy, pytest, flake8)
FROM python:3.12-slim AS dev
WORKDIR /app
COPY requirements.txt requirements-dev.txt ./
RUN pip install --no-cache-dir -r requirements-dev.txt
COPY ./app ./app
COPY ./tests ./tests

# Stage 2: Imagem final leve só com prod
FROM python:3.12-slim AS prod
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY --from=dev /app/app ./app
CMD uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-5010}
