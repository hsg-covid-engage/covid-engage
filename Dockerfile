FROM tiangolo/meinheld-gunicorn:python3.8
LABEL maintainer="Sebastian Ramirez <tiangolo@gmail.com>"

COPY ./app /app
RUN pip install -r /app/requirements.txt