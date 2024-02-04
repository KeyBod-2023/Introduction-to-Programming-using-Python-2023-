def count_number_of_words_in_file(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            words = text.split()
            word_count = len(words)
            return word_count
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return -1


filename = input("Enter the name of the file:\n")
numWordsInFile = count_number_of_words_in_file(filename)
if numWordsInFile >= 0:
    print("The file '" + filename + "' contains " + str(numWordsInFile) + " words.")
