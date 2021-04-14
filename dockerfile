FROM python:3.9.4-alpine
LABEL maintainer="mkutaysezer@gmail.com"

COPY . /app
WORKDIR /app

RUN apk update
RUN apk add --no-cache jpeg-dev zlib-dev
RUN apk add --no-cache --virtual .build-deps build-base linux-headers
RUN pip install -r requirements.txt

WORKDIR /app/source
CMD ["gunicorn", "-w 4", "app:app"]

