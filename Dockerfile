# Start from the official Python image
FROM python:3-slim

# Expose port 8000
EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

# Create directories for certificates and copy them
RUN mkdir -p /app/certificates
COPY cert.pem /app/certificates/
COPY key.pem /app/certificates/

# Set working directory
WORKDIR /app

# Copy the rest of your application code
COPY . .

# During debugging, this entry point will be overridden
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000", "--ssl-keyfile", "/app/certificates/key.pem", "--ssl-certfile", "/app/certificates/cert.pem"]
