import shutil

# e.g. C:\Users\makho\PycharmProjects\IntroductionToProgrammingWithPythonKeyBod\2. Lesson 2\Model Answers\3. Directory Mover\Source Directory (Parent)\Source Directory
sourceDirectory = input("Enter the source path of the directory: ")

# e.g. C:\Users\makho\PycharmProjects\IntroductionToProgrammingWithPythonKeyBod\2. Lesson 2\Model Answers\3. Directory Mover\Destination Directory (Parent)
destinationDirectory = input("Enter the destination path of the directory: ")

try:
    shutil.move(sourceDirectory, destinationDirectory)
    print("Moved the directory: " + sourceDirectory + " to " + destinationDirectory)
except Exception as e:
    print("Error: " + e)

print("The end - program done executing.")
