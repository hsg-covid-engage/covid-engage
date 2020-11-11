FROM python:3.8-slim-buster

COPY ./app /app
COPY config.py config.py
RUN pip install -r /app/requirements.txt