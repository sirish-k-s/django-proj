#!/bin/bash

# Activate the virtual environment (if you are using one)
# Replace "path_to_venv" with the actual path to your virtual environment
# source path_to_venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Run database migrations
python manage.py migrate

# Restart the web server (if necessary)
# Replace "web_server_command" with the command to restart your web server (e.g., "sudo systemctl restart nginx")
web_server_command

# Optionally, run any other setup or build steps required for your application

# Deactivate the virtual environment (if you are using one)
#deactivate
