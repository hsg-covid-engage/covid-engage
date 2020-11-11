FROM python:3.8-slim-buster

COPY ./app /app

RUN pip install -r /app/requirements.txt