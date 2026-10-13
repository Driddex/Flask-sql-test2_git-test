FROM python:3.11-slim

WORKDIR /app
RUN pip install Flask requests psycopg[binary]
COPY . .
EXPOSE 8000
CMD ["python", "Server_Core.py"]
