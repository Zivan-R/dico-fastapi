FROM python:3.11-slim

RUN apt-get update \
 && apt-get install -y gcc libmariadb-dev \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# ensure the package is importable
RUN test -f app/__init__.py || touch app/__init__.py

ENV PYTHONUNBUFFERED=1

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]