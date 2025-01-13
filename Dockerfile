# Use the official Python image as the base
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libtesseract-dev \
    libleptonica-dev \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgl1-mesa-glx \
    python3-tk \
    tk-dev \
    libtk8.6 \
    && rm -rf /var/lib/apt/lists/*

# Copy the application files into the container
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the Tesseract path
ENV TESSERACT_CMD=/usr/bin/tesseract

# Command to run the OCR app (adjust if different)
CMD ["python", "ocr_app.py"]
