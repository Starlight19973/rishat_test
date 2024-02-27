FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["gunicorn", "rishat.wsgi:application", "--bind", "0.0.0.0:80"]
