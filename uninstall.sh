#!/bin/bash

REPO_DIR="sovlist"
VENV_DIR="venv"

remove_virtualenv() {
    if [ -d "$VENV_DIR" ]; then
        echo "Removing virtual environment..."
        rm -rf "$VENV_DIR"
        echo "Virtual environment removed."
    else
        echo "No virtual environment found."
    fi
}

remove_repository() {
    if [ -d "$REPO_DIR" ]; then
        echo "Removing repository directory..."
        rm -rf "$REPO_DIR"
        echo "Repository directory removed."
    else
        echo "No repository directory found."
    fi
}

echo "Starting uninstallation..."

remove_virtualenv

remove_repository

echo "Uninstallation complete."
