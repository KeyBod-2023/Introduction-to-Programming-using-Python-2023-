def write_to_text_file(filename, textToWrite):
    with open(filename, 'w') as file:
        file.write(textToWrite)
        print("Successfully wrote the text '" + textToWrite + "' to the file '" + filename + "'.")
