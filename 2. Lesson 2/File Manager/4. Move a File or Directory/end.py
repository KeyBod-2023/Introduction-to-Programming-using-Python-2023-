import shutil


def move_file(source, destination):
    try:
        shutil.move(source, destination)
        print(f"Moved '{source}' to '{destination}' successfully.")
    except Exception as e:
        print(f"Error: {e}")
