FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential gcc libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements/production.txt /app/
RUN pip install --no-cache-dir -r requirements/production.txt

COPY . /app
RUN mkdir -p /app/staticfiles

EXPOSE 10000
CMD ["sh", "./render-start.sh"]
