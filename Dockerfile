# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1  
ENV PYTHONUNBUFFERED=1

# Create work directory
WORKDIR /app

# Copy requirements file first for caching
COPY requirements.txt /app/

# Install dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy rest of the app code
COPY . /app

# Expose the port the app runs on
EXPOSE 5002

# Default command
CMD ["python3", "main.py"]

