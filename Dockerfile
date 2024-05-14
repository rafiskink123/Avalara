# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Python dependencies file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python application code to the working directory
COPY . .

# Expose the port number where the Flask app will run
EXPOSE 5000

# Command to run the Flask application when the container starts
CMD ["python", "date_overlap_api.py"]

