FROM python:3.9

WORKDIR /fastapi-app

COPY README.md .

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app ./app

CMD ["python", "./app/main.py"]
