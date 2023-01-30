
# Initialize a list
list_ = [1, 2, 3, 4, 5]

# Adding an item to the beginning of a list
list_.insert(0, 0)
print("List after adding item to beginning:", list_)

# Adding an item to the end of a list
list_.append(6)
print("List after adding item to end:", list_)

# Displaying all items in a list
print("All items in the list:", list_)

# Deleting all items in a list
list_.clear()
print("List after deleting all items:", list_)

# Determining the number of list items
list_ = [1, 2, 3, 4, 5]
print("Number of items in the list:", len(list_))

# Checking the list for emptiness
if not list_:
    print("List is empty")
else:
    print("List is not empty")

# Deletion of the first item
list_.pop(0)
print("List after deleting first item:", list_)

# Deletion of the last item
list_.pop()
print("List after deleting last item:", list_)
