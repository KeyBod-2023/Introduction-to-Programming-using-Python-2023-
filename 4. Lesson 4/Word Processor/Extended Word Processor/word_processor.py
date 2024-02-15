import os


def create_a_text_file(filename, printLog):
    with open(filename, 'w') as file:
        if printLog:
            print("The file '" + filename + "' has been created successfully.")


def write_to_text_file(filename, textToWrite, printLog):
    with open(filename, 'w') as file:
        file.write(textToWrite)
        if printLog:
            print("Successfully wrote the text '" + textToWrite + "' to the file '" + filename + "'.")


def add_text_to_existing_file(filename, textToWrite, printLog):
    with open(filename, 'a') as file:
        file.write(textToWrite)
        if printLog:
            print("Successfully wrote the text '" + textToWrite + "' to the file '" + filename + "'.")


def delete_file(filename, printLog):
    try:
        os.remove(filename)
        if printLog:
            print(f"File '{filename}' deleted successfully.")
    except FileNotFoundError:
        if printLog:
            print(f"File '{filename}' not found.")
    except Exception as e:
        if printLog:
            print(f"Error: {e}")


def read_from_text_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
        print(content)


# Extension

def is_user_in_file(name, filename):
    with open(filename, 'r') as file:
        for line in file:
            if line.strip() == name:
                return True
    return False


def main():
    add_text_to_existing_file("list_of_users.txt", '', False)
    list_of_users_file = "list_of_users.txt"

    is_login_successful = False
    print("\nWord Processor Program\n")
    print("You'll need to login to use the application.")
    username = input("Enter your username:\n")

    if is_user_in_file(username, list_of_users_file):
        is_login_successful = True

    if not is_login_successful:
        print("You don't have a profile. You need to register to use the application.")
        while True:
            username = input("Enter the username for your profile:\n")
            if is_user_in_file(username, list_of_users_file):
                print("Username taken. Please try a new one!")
            else:
                break
        is_login_successful = True
        add_text_to_existing_file(list_of_users_file, username + "\n", False)

    while is_login_successful:
        user_history_file = username + ".txt"
        add_text_to_existing_file(user_history_file, "Login", False)

        print("\nWord Processor Menu:")
        print("1. Create a new text file")
        print("2. Write to a text file")
        print("3. Add text to an existing text file")
        print("4. Delete a file")
        print("5. Read a file")
        print("6. View history")
        print("7. Exit")

        choice = input("Enter your choice (1-5):\n")

        user_action = ''

        if choice == '1':
            user_action = '1. Create a new text file\n'
            user_filename = input("Enter the name of the file:\n")
            create_a_text_file(user_filename, True)
            add_text_to_existing_file(user_history_file, user_action, False)

        elif choice == '2':
            user_action = '2. Write to a text file\n'
            user_exiting_filename = input("Enter the name of the file:\n")
            user_text_to_write = input("Enter the text that you would like to write:\n")
            write_to_text_file(user_exiting_filename, user_text_to_write, True)
            add_text_to_existing_file(user_history_file, user_action, False)

        elif choice == '3':
            user_action = "3. Add text to an existing text file\n"
            user_exiting_filename = input("Enter the name of the file:\n")
            user_text_to_add = input("Enter the text that you would like to add:\n")
            add_text_to_existing_file(user_exiting_filename, user_text_to_add, True)
            add_text_to_existing_file(user_history_file, user_action, False)

        elif choice == '4':
            user_action = "4. Delete a file\n"
            user_file_to_delete = input("Enter the name of the file:\n")
            delete_file(user_file_to_delete, True)
            add_text_to_existing_file(user_history_file, user_action, False)

        elif choice == '5':
            user_action = "5. Read a file\n"
            user_file_to_read = input("Enter the name of the file:\n")
            read_from_text_file(user_file_to_read)
            add_text_to_existing_file(user_history_file, user_action, False)

        elif choice == '6':
            user_action = "6. View history\n"
            print("Here is your history:")
            read_from_text_file(user_history_file)
            print("=== This is the end ===")
            add_text_to_existing_file(user_history_file, user_action, False)

        elif choice == '7':
            user_action = "6. Exit\n"
            is_login_successful = False
            print("Exiting Word Processor. Goodbye!")
            add_text_to_existing_file(user_history_file, user_action, False)

        else:
            user_action = "Entered invalid choice\n"
            print("Invalid choice. Please enter a number between 1 and 6.")
            add_text_to_existing_file(user_history_file, user_action, False)
main()
