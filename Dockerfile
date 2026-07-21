FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy project files
COPY . .

# Create staticfiles directory and copy Django admin static assets
RUN mkdir -p /app/staticfiles && \
    python -c "import os, shutil; from django.contrib import admin; source = os.path.join(os.path.dirname(admin.__file__), 'static', 'admin'); dest = '/app/staticfiles/admin'; shutil.copytree(source, dest, dirs_exist_ok=True) if os.path.exists(source) else print('Admin static source not found')"

# Copy and make entrypoint executable
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["/entrypoint.sh"]
