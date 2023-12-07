welcomeMessage = ("**** Welcome to our mini program. We have 4 options as listed below:\n "
                  "1. Addition\n"
                  "2. Subtraction\n"
                  "3. Division\n"
                  "4. Multiplication\n"
                  ""
                  "Please select an option from the ones above.\n"
                  "Your option: ")

userChoice = input(welcomeMessage)
numberOne = int(input("Enter the first number:\n"))
numberTwo = int(input("Enter the second number:\n"))

if userChoice == '1':
    print("The sum is: " + str(numberOne + numberTwo))

elif userChoice == '2':
    print("The difference is: " + str(numberOne - numberTwo))

elif userChoice == '3':
    print("The quotient is: " + str(numberOne / numberTwo))

elif userChoice == '4':
    print("The product is: " + str(numberOne * numberTwo))

print("Program shutting down! Please run it again if you'd like.")
