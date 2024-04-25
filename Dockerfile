FROM python:3.10-slim

COPY works /app/works
COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8000

CMD python works/manage.py runserver 0.0.0.0:8000