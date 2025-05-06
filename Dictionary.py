#Example on dict.get(key, default=none)
my_dict = {"name": "Nikodimos", "age": 25}
print(my_dict.get("age"))           # Output: 25
print(my_dict.get("gender", "N/A")) # Output: N/A

#Example on dict.keys()
my_dict = {"a": 1, "b": 2}
print(my_dict.keys())  # Output: dict_keys(['a', 'b'])

#Example on dict.items()
my_dict = {"x": 10, "y": 20}
print(my_dict.items())  # Output: dict_items([('x', 10), ('y', 20)])

#Example on dict.update(other_dict)
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
d1.update(d2)
print(d1)  # Output: {'a': 1, 'b': 3, 'c': 4}
