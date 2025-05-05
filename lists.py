# Example for append()
fruits = ["apple", "banana"]
fruits.append("orange")
print(fruits)  

# Example for extend()
numbers = [1, 2]
numbers.extend([3, 4])
print(numbers)  

# Example for insert()
colors = ["red", "blue"]
colors.insert(1, "green")
print(colors)  

# Example for remove()
animals = ["cat", "dog", "cat"]
animals.remove("cat")
print(animals)  

# Example for pop()
stack = [1, 2, 3]
last = stack.pop()
print(last, stack) 

# Example for clear()
items = [1, 2, 3]
items.clear()
print(items)  

# Example for index()
fruits = ['apple', 'banana', 'cherry']
pos = fruits.index('banana')
print(pos)

#Example for count()
nums = [1, 2, 2, 3, 2]
count_2 = nums.count(2)
print(count_2)

#Example for reverse()
names = ['Alice', 'Bob', 'Charlie']
names.reverse()
print(names)

#Example for sort()
scores = [40, 10, 30, 20]
scores.sort()
print(scores)
scores.sort(reverse=True)
print(scores)

#Example for copy()
original = [1, 2, 3]
duplicate = original.copy()
duplicate.append(4)
print(original)
print(duplicate)

#Example for list.__len__()
items = ['pen', 'book', 'eraser']
size = len(items)
print(size)

#Example for list.__getitem__(index)
nums = [10, 20, 30]
value = nums[1]
print(value)

#Example for list.__setitem__(index, value)
letters = ['a', 'b', 'c']
letters[1] = 'z'
print(letters)

#Example for list.__delitem__(index)
names = ['Tom', 'Jerry', 'Spike']
del names[0]
print(names)

#Examples for zip(list1,list2)
names = ['Alice', 'Bob']
ages = [25, 30]
combined = list(zip(names, ages))
print(combined)














