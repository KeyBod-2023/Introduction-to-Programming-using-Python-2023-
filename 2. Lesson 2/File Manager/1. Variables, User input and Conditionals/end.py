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
            # TODO: Create a new text file
            pass

        elif choice == '2':
            # TODO: Create a new directory
            pass

        elif choice == '3':
            # TODO: Move a file or directory
            pass

        elif choice == '4':
            # TODO: Delete a file
            pass

        elif choice == '5':
            # TODO: Delete a directory
            pass

        elif choice == '6':
            print("Exiting File Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


main()
