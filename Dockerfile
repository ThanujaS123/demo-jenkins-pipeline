# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy your application file into the container
COPY app.py /app/

# Define the command to run your app
CMD ["python", "app.py"]
