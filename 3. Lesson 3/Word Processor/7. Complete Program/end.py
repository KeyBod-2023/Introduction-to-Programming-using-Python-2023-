import os


def create_a_text_file(filename):
    with open(filename, 'w') as file:
        print("The file '" + filename + "' has been created successfully.")


def write_to_text_file(filename, textToWrite):
    with open(filename, 'w') as file:
        file.write(textToWrite)
        print("Successfully wrote the text '" + textToWrite + "' to the file '" + filename + "'.")


def add_text_to_existing_file(filename, textToWrite):
    with open(filename, 'a') as file:
        file.write(textToWrite)
        print("Successfully wrote the text '" + textToWrite + "' to the file '" + filename + "'.")


def delete_file(filename):
    try:
        os.remove(filename)
        print(f"File '{filename}' deleted successfully.")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"Error: {e}")


def read_from_text_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
        print(content)


def main():
    while True:
        print("\nWord Processor Menu:")
        print("1. Create a new text file")
        print("2. Write to a text file")
        print("3. Add text to an existing text file")
        print("4. Delete a file")
        print("5. Read a file")
        print("6. Exit")

        choice = input("Enter your choice (1-5):\n")

        if choice == '1':
            user_filename = input("Enter the name of the file:\n")
            create_a_text_file(user_filename)
            pass

        elif choice == '2':
            user_exiting_filename = input("Enter the name of the file:\n")
            user_text_to_write = input("Enter the text that you would like to write:\n")
            write_to_text_file(user_exiting_filename, user_text_to_write)
            pass

        elif choice == '3':
            user_exiting_filename = input("Enter the name of the file:\n")
            user_text_to_add = input("Enter the text that you would like to add:\n")
            add_text_to_existing_file(user_exiting_filename, user_text_to_add)
            pass

        elif choice == '4':
            user_file_to_delete = input("Enter the name of the file:\n")
            delete_file(user_file_to_delete)
            pass

        elif choice == '5':
            user_file_to_read = input("Enter the name of the file:\n")
            read_from_text_file(user_file_to_read)

        elif choice == '6':
            print("Exiting Word Processor. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


main()
