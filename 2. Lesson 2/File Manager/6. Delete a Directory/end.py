import shutil


def delete_directory(directory):
    try:
        shutil.rmtree(directory)
        print(f"Directory '{directory}' deleted successfully.")
    except FileNotFoundError:
        print(f"Directory '{directory}' not found.")
    except Exception as e:
        print(f"Error: {e}")
