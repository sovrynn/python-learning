# Defining a 2D list (list of lists)
list_of_lists = [[1, 2], [3, 4], [5, 6]]

# Print out list_of_lists
print(list_of_lists)

# What is the shape of list_of_lists?
print('Length of list_of_lists: %d' % len(list_of_lists))
print('Length of first list in list_of_lists: %d' % len(list_of_lists[0]))
print('Length of second list in list_of_lists: %d' % len(list_of_lists[1]))

# Iterating over each list in list_of_lists
for list in list_of_lists:
    print(list)

# Iterating over each element in list_of_lists
for list in list_of_lists:
    for num in list:
        print(num)
