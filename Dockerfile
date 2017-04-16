FROM python:2.7

COPY feeds/requirements.txt /data/src/requirements.txt

RUN pip install -r /data/src/requirements.txt
