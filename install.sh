#!/bin/bash

# Exit on any error
set -e

# Function to display error message and exit
error_exit() {
    echo "Error: $1"
    exit 1
}

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    error_exit "Python 3 is not installed. Please install Python 3 and try again."
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    error_exit "pip3 is not installed. Please install pip3 and try again."
fi

# Create a virtual environment
echo "Creating virtual environment..."
python3 -m venv env || error_exit "Failed to create virtual environment."

# Activate the virtual environment
echo "Activating virtual environment..."
source env/bin/activate || error_exit "Failed to activate virtual environment."

# Upgrade pip in the virtual environment
echo "Upgrading pip..."
pip install --upgrade pip || error_exit "Failed to upgrade pip."

# Install required Python packages
echo "Installing required packages..."
pip install scapy || error_exit "Failed to install scapy."

# Additional packages can be added here
# pip install <other-package> || error_exit "Failed to install <other-package>."

echo "All dependencies installed successfully."

# Deactivate the virtual environment
deactivate || error_exit "Failed to deactivate virtual environment."

echo "Setup complete. To use the virtual environment, run 'source env/bin/activate'."
