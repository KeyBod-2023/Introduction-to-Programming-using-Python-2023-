welcomeMessage = ("**** Welcome to our mini program. We have 4 options as listed below:\n "
                  "1. Addition\n"
                  "2. Subtraction\n"
                  "3. Division\n"
                  "4. Multiplication\n"
                  ""
                  "Please select an option from the ones above.\n"
                  "Your option: ")

userChoice = input(welcomeMessage)

if userChoice == "1":
    print("Performing addition.")

elif userChoice == "2":
    print("Performing subtraction.")

elif userChoice == "3":
    print("Performing division.")

elif userChoice == "4":
    print("Performing multiplication.")
else:
    print("Invalid option!")

print("Done!!")
