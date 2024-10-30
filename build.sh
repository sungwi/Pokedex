#!/bin/bash

# Install pip
echo "Installing pip..."
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3.9 get-pip.py

# Install dependencies
echo "Installing project dependencies..."
python3.9 -m pip install -r requirements.txt

# Make migrations
echo "Running migrations..."
python3.9 manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
python3.9 manage.py collectstatic --noinput --clear

echo "Build process completed!"