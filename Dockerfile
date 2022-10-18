FROM python:3.9

WORKDIR /fastapi-app

COPY README.md .

COPY requirements.txt .

COPY .env .

RUN pip install -r requirements.txt

COPY ./app ./app

COPY ./test ./test

RUN pip --disable-pip-version-check list --format=freeze

CMD ["python", "./app/main.py"]
