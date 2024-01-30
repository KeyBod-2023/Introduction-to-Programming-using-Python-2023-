def add_text_to_existing_file(filename, textToWrite):
    with open(filename, 'a') as file:
        file.write(textToWrite)
        print("Successfully wrote the text '" + textToWrite + "' to the file '" + filename + "'.")
