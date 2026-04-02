FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

# Create staticfiles directory and copy Django admin static files
RUN mkdir -p /app/staticfiles && \
    python -c "import os, shutil; from django.contrib import admin; source = os.path.join(os.path.dirname(admin.__file__), 'static', 'admin'); dest = '/app/staticfiles/admin'; shutil.copytree(source, dest) if os.path.exists(source) else print('Source not found')"

# Run collectstatic
RUN python manage.py collectstatic --no-input
RUN python manage.py makemigrations
RUN python manage.py migrate

EXPOSE 8000

CMD ["gunicorn", "bank_site.wsgi:application", "--bind", "0.0.0.0:8000"]
