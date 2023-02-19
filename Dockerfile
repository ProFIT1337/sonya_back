FROM python:3.8

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update \
    && apt install -y postgresql gcc python3-dev python3-setuptools musl-dev python3-pillow musl

RUN apt install -y musl-dev libffi-dev

RUN apt install -y libffi-dev cargo

RUN apt install -y gcc musl-dev

RUN pip install --upgrade pip setuptools wheel
RUN pip install ez_setup
COPY ./requirements.txt .
RUN pip install -r requirements.txt
