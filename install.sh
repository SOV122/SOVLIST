#!/bin/bash

sudo apt-get update -y

if ! command -v python3 >/dev/null 2>&1; then
    sudo apt-get install -y python3 python3-pip
fi

if ! command -v virtualenv >/dev/null 2>&1; then
    sudo pip3 install virtualenv
fi

virtualenv venv -p python3
source venv/bin/activate

pip install --upgrade pip

deactivate
