FROM python:3.9

WORKDIR /fastapi-app

COPY README.md .

COPY poetry.lock .

COPY pyproject.toml .

COPY requirements.txt .

RUN python -m venv venv

RUN source venv/Script/activate

RUN pip install poetry

RUN poetry install

COPY ./app ./app

COPY ./test ./test

CMD ["python", "./app/main.py"]
