my_list = [1, 2, 3, 'apple']
my_list.remove(2)
print("List after removing 2: " + str(my_list))

popped_element = my_list.pop(1)
print("Popped element: " + str(popped_element))
print("List after popping an element: " + str(my_list))

print("List before deleteing item at index 0: " + str(my_list))
del my_list[0]
print("List after deleting item at index 0: " + str(my_list))