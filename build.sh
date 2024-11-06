#!/bin/bash

# Install pip
echo "Installing pip..."
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3.9 get-pip.py

# Install dependencies
echo "Installing project dependencies..."
python3.9 -m pip install -r requirements.txt

# # Djangoのcontribアプリを一時的にコメントアウト
# sed -i '' 's/^    '\''django.contrib./#&/' pokemonkawasaki/settings.py

# # Make migrations
# echo "Making migrations..."
# python3.9 manage.py makemigrations

# # Apply migrations
# echo "Running migrations..."
# python3.9 manage.py migrate --noinput

# # コメントアウトを解除して元に戻す
# sed -i '' 's/^#    '\''django.contrib./    '\''django.contrib./' pokemonkawasaki/settings.py

# Collect static files
echo "Collecting static files..."
python3.9 manage.py collectstatic --noinput --clear

echo "Build process completed!"