my_list = [4, 2, 8, 3, 8]

length = len(my_list)
print("Length of list: " + str(length))

my_list.sort()
print("Sorted list: " + str(my_list))

my_list.reverse()
print("List sorted in reverse: " + str(my_list))

count_eight = my_list.count(8)
print("Count occurrences of 8 are: " + str(count_eight))