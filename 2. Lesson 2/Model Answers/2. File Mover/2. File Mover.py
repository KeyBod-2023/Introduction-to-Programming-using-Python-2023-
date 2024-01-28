import shutil

# e.g. C:\Users\makho\PycharmProjects\IntroductionToProgrammingWithPythonKeyBod\2. Lesson 2\Model Answers\2. File Mover\File Source Directory\FileToMove.txt
sourceFile = input("Enter the source path of the file: ")

# e.g. C:\Users\makho\PycharmProjects\IntroductionToProgrammingWithPythonKeyBod\2. Lesson 2\Model Answers\2. File Mover\File Destination Directory
destinationFile = input("Enter the destination path of the file: ")

try:
    shutil.move(sourceFile, destinationFile)
    print("Moved the file: " + sourceFile + " to " + destinationFile)
except Exception as e:
    print("Error: " + e)

print("The end - program done executing.")
