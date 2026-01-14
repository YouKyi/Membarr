FROM python:3.11-alpine

WORKDIR /app

RUN apk --no-cache add --quiet \
    openssl \
    bash

RUN pip install --no-cache-dir --upgrade pip setuptools wheel

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN adduser -D -u 1000 membarr && \
    chown -R membarr:membarr /app

USER membarr

CMD ["python", "-u", "run.py"]
