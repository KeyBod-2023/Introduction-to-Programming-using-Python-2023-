def is_user_in_file(name, filename):
    with open(filename, 'r') as file:
        for line in file:
            if line.strip() == name:
                return True
    return False


# print("Is Vusani in file? " + str(is_user_in_file("Vusani", "users.txt")))