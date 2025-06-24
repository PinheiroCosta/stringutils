# Stage 1: Dev com Poetry
FROM python:3.12-slim AS dev
RUN apt update && apt install -y curl gcc libffi-dev libpq-dev
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"
WORKDIR /app
COPY pyproject.toml poetry.lock README.md ./
RUN poetry config virtualenvs.create false \
 && poetry install --no-interaction --no-ansi --no-root
COPY ./app ./app
COPY ./tests ./tests

# Stage 2: Runtime leve
FROM python:3.12-slim AS prod
WORKDIR /app
COPY --from=dev /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY ./app ./app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "${PORT:-5010}"]
