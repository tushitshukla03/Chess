#!/bin/bash

import os
import subprocess
import sys


def in_venv():
    return sys.prefix != sys.base_prefix
# Define the path for the virtual environment
venv_path = os.path.join(os.getcwd(), 'venv')

# Function to create a virtual environment


# Function to install requirements
def install_requirements(path):
    subprocess.run(['pip3', 'install', '-r', 'requirements.txt'])

# Function to run the chess AI script


# Main script
if __name__ == '__main__':
    try:
    # Check for venv
        if in_venv():
            print('Using Virtualenv')
        else:
            print('Not using Virtualenv')
            exit()
    
        print("Activating virtual environment and installing requirements...")
        install_requirements(venv_path)
    
        print("Running chess AI...")
        subprocess.run(['python3', 'ChessMain.py'])
    except KeyboardInterrupt:
        print("Process is interrupted")

