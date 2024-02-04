def count_lines_in_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            line_count = len(lines)
            return line_count
    except FileNotFoundError:
        print("Error: The file '" + filename + "' does not exist.")
        return -1

userFilename = input("Enter the filename to count lines:\n")
fileLineCount = count_lines_in_file(userFilename)
if fileLineCount >= 0:
    print("The file '" + userFilename + "' contains " + str(fileLineCount) + " lines.")
