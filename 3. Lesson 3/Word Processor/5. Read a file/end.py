def read_from_text_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
        print(content)

