import shutil

# e.g. C:\Users\makho\PycharmProjects\IntroductionToProgrammingWithPythonKeyBod\2. Lesson 2\Model Answers\5. File Copy Utility\File Source Directory\FileToCopy.txt
sourcePathFile = input("Enter the source path of the file that you would like to copy:\n")

# e.g. C:\Users\makho\PycharmProjects\IntroductionToProgrammingWithPythonKeyBod\2. Lesson 2\Model Answers\5. File Copy Utility\File Destination Directory
destinationPathFile = input("Enter the destination path of the file:\n")

try:
    shutil.copy(sourcePathFile, destinationPathFile)
    print("Copied the file: " + sourcePathFile + " to " + destinationPathFile)
except Exception as e:
    print("Error: " + e)

print("The end - program done executing.")
