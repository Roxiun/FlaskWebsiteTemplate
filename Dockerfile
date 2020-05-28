FROM python:3.6-alpine

RUN mkdir /project
WORKDIR /project
ADD . /project


RUN pip install -r requirements.txt

ENV FLASK_APP app.py

EXPOSE 5000
CMD flask run --host=0.0.0.0
