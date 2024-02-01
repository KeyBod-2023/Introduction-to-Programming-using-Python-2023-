def create_a_text_file(filename):
    file = open(filename, 'w')
    print("The file '" + filename + "' has been created successfully.")
    file.close()

    # with open(filename, 'w') as file:
    #     print("The file '" + filename + "' has been created successfully.")


create_a_text_file("Lesson 3 filename - 2.txt")
