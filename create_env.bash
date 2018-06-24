#!/bin/bash

# Create the virtual environment
virtualenv -p python3 krpc-env
source krpc-env/bin/activate
pip3 install -r requirements.txt
