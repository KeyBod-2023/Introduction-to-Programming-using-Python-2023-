def is_user_in_file(name, filename):
    users = []
    with open(filename, 'r') as file:
        for line in file:
            users.append(line.strip())

    for user in users:
        if user == name:
            return True

    return False


# print("Is Vusani in file? " + str(is_user_in_file("Vusani", "users.txt")))