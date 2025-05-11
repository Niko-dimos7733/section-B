#Example on dict.get(key, default=none)
my_dict = {"name": "Nikodimos", "age": 25}
print(my_dict.get("age"))           # Output: 25
print(my_dict.get("gender", "M/F")) # Output: M/F

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

#Example on dict.values()
my_dict = {"a": 10, "b": 20}
print(my_dict.values())  # Output: dict_values([10, 20])

#Example on dict.pop(key, default=None)
my_dict = {"x": 100, "y": 200}
val = my_dict.pop("x")
print(val)       # Output: 100
print(my_dict)   # Output: {'y': 200}

#Example on dict.popitem()
my_dict = {"a": 1, "b": 2}
pair = my_dict.popitem()
print(pair)      # Output: ('b', 2)
print(my_dict)   # Output: {'a': 1}

#Example on dict.clear()
my_dict = {"foo": "bar"}
my_dict.clear()
print(my_dict)  # Output: {}
