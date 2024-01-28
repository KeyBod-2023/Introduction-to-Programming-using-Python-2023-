filename = input("Enter the name of the file:\n")

try:
    file = open(filename, "r")
except FileNotFoundError:
    print("The file doesn't exist! Please create it and open again!")

print("The end - program done executing.")
