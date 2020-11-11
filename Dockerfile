FROM tiangolo/meinheld-gunicorn:python3.8

COPY ./app /app

RUN pip install -r /app/requirements.txt