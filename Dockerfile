FROM python:2.7

RUN apt-get update && apt-get install -y netcat

ENV PYTHONUNBUFFERED 1

RUN mkdir /forex_backend

WORKDIR /forex_backend

ADD requirements.txt /forex_backend/

RUN pip install -r requirements.txt

ADD . /forex_backend/

RUN rm db.sqlite3

RUN chmod +x /forex_backend/runserver.sh

CMD ["sh", "runserver.sh", "postgres", "5432", "60"]
