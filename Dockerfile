FROM python:3.14.2

ENV TZ JST-9
ENV PYTHONUNBUFFERED 1

RUN python3 -m pip install --upgrade pip
COPY requirements.txt /tmp/requirements.txt
RUN python3 -m pip install -r /tmp/requirements.txt

WORKDIR /opt/app/
COPY app/ /opt/app/

ENTRYPOINT ["python3", "app.py"]