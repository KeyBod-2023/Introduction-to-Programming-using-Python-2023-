my_set = {1, 2, 3}
length = len(my_set)
print("Length of set: " + str(length))

is_subset = {1, 2}.issubset(my_set)
print("is {1, 2} a subset of " + str(my_set) + " ? " + str(is_subset))

is_superset = my_set.issuperset({1, 2})
print("is " + str(my_set) + " a superset of {1, 2} ? " + str(is_superset))