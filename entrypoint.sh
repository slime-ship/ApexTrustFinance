#!/bin/sh

set -e

echo "Waiting for database..."

# Apply database migrations
echo "Applying migrations..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Create admin user
echo "Creating admin user..."
python manage.py create_admin || echo "Admin already exists or creation skipped."

echo "Starting Gunicorn..."

exec gunicorn bank_site.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3
