# Use an official Python base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all source code to the container
COPY . .

# Run unit tests to ensure everything is fine (CI step)
RUN pytest -v

# Default command (you can modify later)
CMD ["python3"]
