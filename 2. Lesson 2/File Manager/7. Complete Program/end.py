import os
import shutil


def create_text_file(filename):
    with open(filename, 'w') as file:
        print(f"Text file '{filename}' created successfully.")


def create_directory(directory):
    os.makedirs(directory, exist_ok=True)
    print(f"Directory '{directory}' created successfully.")


def move_file(source, destination):
    try:
        shutil.move(source, destination)
        print(f"Moved '{source}' to '{destination}' successfully.")
    except Exception as e:
        print(f"Error: {e}")


def delete_file(filename):
    try:
        os.remove(filename)
        print(f"File '{filename}' deleted successfully.")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"Error: {e}")


def delete_directory(directory):
    try:
        shutil.rmtree(directory)
        print(f"Directory '{directory}' deleted successfully.")
    except FileNotFoundError:
        print(f"Directory '{directory}' not found.")
    except Exception as e:
        print(f"Error: {e}")


def main():
    while True:
        print("\nFile Manager Menu:")
        print("1. Create a new text file")
        print("2. Create a new directory")
        print("3. Move a file or directory")
        print("4. Delete a file")
        print("5. Delete a directory")
        print("6. Exit")

        choice = input("Enter your choice (1-6):\n")

        if choice == '1':
            user_filename = input("Enter the name of the file:\n")
            create_text_file(user_filename)
            pass

        elif choice == '2':
            user_directory = input("Enter the name of the directory:\n")
            create_directory(user_directory)
            pass

        elif choice == '3':
            user_file_or_directory_source = input("Enter the source location of the file or directory\n")
            user_file_or_directory_destination = input("Enter the destination location of the file or directory:\n")
            move_file(user_file_or_directory_source, user_file_or_directory_destination)
            pass

        elif choice == '4':
            user_file_to_delete = input("Enter the name of the file:\n")
            delete_file(user_file_to_delete)
            pass

        elif choice == '5':
            user_directory_to_delete = input("Enter the name of the directory:\n")
            delete_directory(user_directory_to_delete)
            pass

        elif choice == '6':
            print("Exiting File Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
    print()


main()
