FROM python:3.9-slim

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml /app

RUN poetry install

COPY . /app

CMD ["poetry", "run", "task", "start"]
