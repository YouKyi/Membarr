FROM python:3.11-alpine

WORKDIR /app

# Optimisation & Sécurité :
# 1. On combine les RUN pour corriger DL3059 (moins de layers)
# 2. On ignore DL3018 (versions apk) et DL3013 (versions pip) car on veut les dernières maj de sécu
# hadolint ignore=DL3018,DL3013
RUN apk --no-cache add --quiet openssl bash && \
    pip install --no-cache-dir --upgrade pip setuptools wheel

# Copie des requirements
COPY requirements.txt .

# Installation des dépendances
# DL3059 est ignoré ici car on sépare exprès pour le cache Docker
# hadolint ignore=DL3059
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Création user non-root
RUN adduser -D -u 1000 membarr && \
    chown -R membarr:membarr /app

USER membarr

CMD ["python", "-u", "run.py"]
