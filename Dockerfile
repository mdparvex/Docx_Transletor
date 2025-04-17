# Use an official Python runtime as a base image
FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

# Start the Flask server
CMD ["python", "app.py"]
