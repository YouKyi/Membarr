FROM python:3.11-alpine

# Install only runtime dependencies
RUN apk --no-cache add --quiet \
    openssl \
    bash

WORKDIR /app

# Copy and install dependencies first (better cache)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create non-root user for security
RUN adduser -D -u 1000 membarr && \
    chown -R membarr:membarr /app
USER membarr

CMD ["python", "-u", "run.py"]
