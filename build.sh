#!/bin/bash

# Update pip
echo "Updating pip..."
python3.10 -m pip install -U pip

# Install dependencies
echo "Installing dependencies..."
python3.10 -m pip install -r requirements.txt

# Apply migrations
echo "Applying migrations..."
python3.10 manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
python3.10 manage.py collectstatic --noinput --clear

echo "Build process completed!"