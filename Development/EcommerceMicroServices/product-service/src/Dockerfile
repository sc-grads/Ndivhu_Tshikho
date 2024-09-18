# Use the official Python image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port for the product-service
EXPOSE 8001

# Run the product service
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8001"]
