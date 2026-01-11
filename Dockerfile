FROM python:3.11-alpine

RUN \
    echo "http://dl-8.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories && \
    echo "http://dl-8.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories

# Install basic dependencies
RUN \
    apk --no-cache add -q git cloc openssl openssl-dev openssh alpine-sdk bash gettext sudo build-base gnupg linux-headers xz

WORKDIR /app
COPY . .
RUN pip install -Ur requirements.txt
CMD ["python", "-u", "run.py"]
