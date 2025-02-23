# Use the official Python image matching local version
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy the entire project to the container
COPY . /app

# Install system dependencies (if required)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Ensure the `app` module is found (fixes import issues)
ENV PYTHONPATH=/app

# Expose necessary ports
EXPOSE 8000 8501

# Run FastAPI and Streamlit with proper JSON CMD format
CMD ["sh", "-c", "uvicorn server:app --host 0.0.0.0 --port 8000 & streamlit run main.py --server.port 8501 --server.address 0.0.0.0"]
