# section-B
String Quotation Examples in Python
Single quotes (') for basic strings.

Double quotes (") for strings that contain single quotes (like contractions).

Triple quotes (""" """) for multi-line strings or strings that contain both single and double quotes.

# string.upper()
- Converts all characters in a string to uppercase.
- Useful when you want to normalize or compare strings without worrying about case.

# string.lower()
- Converts all characters in a string to lowercase.
- Useful for case-insensitive comparisons, search, or formatting.

# String.title()
- Converts the first character of each word in the string to uppercase and the rest to lowercase.
- Commonly used to format names, titles, or headings.

# String.capitalize()
- Converts the first character of the string to uppercase, and the rest to lowercase.
Good for formatting sentences or names.

# String.swapcase()
- Swaps the case of each letter:
- Uppercase → lowercase
- Lowercase → uppercase

# String.find()
- Searches for a substring in the string and returns the index of its first occurrence.
- If not found, it returns -1.

# string.index()
- Returns the first index where the substring sub is found
- Throws ValueError if sub is not found.

# string.startswith()
- Checks if the string starts with the given prefix.
- Returns True or False.

# string.endswith()
- Checks if the string ends with the given suffix.
- Returns True or False.

# string.count()
- Returns the number of times sub or character appears in the string.

# string.replace()
- Returns a new string where occurrences of old are replaced with new.
- Optional: limit replacements with count.

# string.strip()
- Removes leading and trailing characters
- If chars is provided, removes any of those characters from both ends.

# string.lstrip()
- Removes characters from the left side of a string.
- If no argument is given, it removes whitespace (spaces, tabs, newlines).
- If you provide a string as an argument, it removes all matching characters from the start, not a prefix.

# string.rstrip()
- Removes characters from the right side of a string.
- Behaves like lstrip() but on the end.
- Useful for cleaning up trailing spaces, symbols, or newlines.

# string.split()
- Breaks a string into a list of parts based on a separator.
- Default separator is any whitespace.

# string.join()
- Joins elements in an iterable (like a list) into one string.
- The string it’s called on is placed between each element.

# string.isalpha()
- Returns True if all characters are alphabetic (a-z, A-Z) and the string is not empty.
- Returns False if it contains numbers, spaces, or symbols.

# string.isdigit()
- Returns True if all characters are digits (0-9) and the string is not empty.
- Doesn’t accept decimal points or negative signs — just digits.

# string.isalnum()
- Checks if all characters are letters or digits (no spaces or symbols).
- Returns True or False.

# string.isspace()
- Checks if the entire string is made up of whitespace characters.
- Returns True or False.

# string.format()
- Inserts values into placeholders using {}.
More verbose than f-strings but still works.

# f-strings
- Modern way to format strings using f"text {var}".
- Cleaner, faster, and preferred over string.format().

# len()
- Returns the number of characters in a string (or items in a list).
- Simple and essential.

# string.encode()
- Converts a string into bytes (default UTF-8).
Useful for files, networks, etc.




