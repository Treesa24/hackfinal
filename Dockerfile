FROM python:3.11-slim

# Install system deps for OCR
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libtesseract-dev \
    && rm -rf /var/lib/apt/lists/*

# 👇 IMPORTANT: work inside backend
WORKDIR /app/backend

# Install Python deps
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy backend code
COPY backend backend

# Start FastAPI
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
