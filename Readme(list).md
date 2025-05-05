# list.append()
- Adds a single item to the end of the list.
- Simple way to grow a list.

# list.extend()
- Adds all items from an iterable (like another list) to the end of the list.
- Useful for combining lists or iterables.

# list.insert()
- Inserts an item at a specified index, shifting other items to the right.
- Precise control over item placement.

# list.remove()
- Removes the first occurrence of a specified item from the list.
- Handy for deleting by value, but raises an error if item isn’t found.

# list.pop()
- Removes and returns an item at a given index (defaults to the last item).
- Useful for retrieving and removing items, like a stack.

# list.clear()
- Removes all items from the list, leaving it empty.
- Quick way to reset a list.

# list.index()
- Returns the index of the first occurrence of item x.

# list.count()
- Returns the number of times item x appears in the list.
- Handy for frequency checks.

# list.reverse()
- Reverses the list in place (modifies the original list).

# list.sort()
- Sorts the list in ascending order by default.
- Use reverse=True to sort in descending order.

# list.copy()
- Returns a shallow copy of the list (not linked to the original).
- Useful when you want to modify a list without affecting the original.

# list.__len__()
- Returns the number of items in the list.
- Most commonly used with the built-in len() function.

# list.__getitem__(index)
- Retrieves the item at the given index.
- Same as using square brackets.

# list.__setitem__(index, value)
- Assigns a value to the item at a specific index.
- Common for updating list content.

# list.__delitem__(index)
- Deletes the item at the specified index.
- Shortcut is using del.

# Zip(list1,list2)
- Combines two (or more) lists element-wise into tuples.
- Stops at the length of the shortest list.