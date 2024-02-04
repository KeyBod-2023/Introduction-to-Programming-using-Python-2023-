def get_file_contents(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        print("Error: The file '" + filename + "' does not exist.")
        return -1


userFilename = input("Enter the filename that you want to display:\n")
fileContents = get_file_contents(userFilename)
if fileContents != -1:
    print(fileContents)
