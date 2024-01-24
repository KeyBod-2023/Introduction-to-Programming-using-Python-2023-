import os


def create_directory(directory):
    os.makedirs(directory, exist_ok=True)
    print(f"Directory '{directory}' created successfully.")
