#!/bin/bash

# Navigate to the project directory
cd /mnt/ssd2/hillel_pro || exit

# Pull the latest code from the repository
git pull origin main

# Navigate to the bot directory
cd /mnt/ssd2/hillel_pro/tbot || exit

# Activate the virtual environment
source venv/bin/activate

# Install required dependencies
pip install -r requirements.txt

sudo systemctl restart tbot.service


# Print success message
echo "? Bot successfully updated and restarted!"