# Use a base image with your desired programming language and version
FROM python:3.9

# Set the working directory inside the container
WORKDIR /code/app

# Copy the necessary files from your local machine to the container
COPY ./requirements.txt ./requirements.txt

# Install any dependencies required by your backend
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the app directory into the working directory
COPY ./app .

# Define the command to start your backend application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]