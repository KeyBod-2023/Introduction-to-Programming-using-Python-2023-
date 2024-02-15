def copy_file_contents(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as input_file:
            content = input_file.read()
            with open(output_filename, 'w') as output_file:
                output_file.write(content)
        print(f"Content copied from '{input_filename}' to '{output_filename}' successfully.")
    except FileNotFoundError:
        print("Error: One or both of the files do not exist.")


firstFilename = input("Enter the name of the first file:\n")
secondFilename = input("Enter the name of the second file:\n")

copy_file_contents(firstFilename, secondFilename)