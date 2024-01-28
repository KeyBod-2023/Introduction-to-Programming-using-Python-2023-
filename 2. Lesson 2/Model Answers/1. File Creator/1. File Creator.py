filename = input("Enter the name of the text file:\n")  # e.g. Testing2024
userMessage = input("Enter the message that you would like to write:\n")  # e.g. Thi is for testing in 2024

with open(filename, 'w') as file:
    file.write(userMessage)
    print("Message written to the file successfully.")

print("The end - program done executing.")
