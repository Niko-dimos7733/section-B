# Examples for single, double and Triple quotes
#Single quote
string = 'hello world'
print(string)
#Double quote 
stringg = "He's a doctor"
print(stringg)
#Triple quote
stringgg = """ My teacher once said to me "The only permanent thing is change So, learn to adapt."and it stuck in my mind"""
print(stringgg)

# Example for string.upper()
name = "Nikodimos Bacos"
print (name.upper())

# Example for string.lower()
user = "HELLO"
print (user.lower())

# Example for string.title()
Psalm1 = "I have been young, and now am old; yet have I not seen the righteous forsaken, nor his seed begging bread."
print (Psalm1.title())

# Example for str.capitalize()
God = "jesus CHRIST"
print(God.capitalize())

# Example for str.swapcase()
Psalm2 = "'tHE lORD IS MY SHEPHERD; i LACK NOTHING.'"
print(Psalm2.swapcase())

#Example for str.find()
Psalm3 = "For whosoever hath, to him shall be given, and he shall have more abundance: but whosoever hath not, from him shall be taken away even that he hath."
print(Psalm3.find('abundance'))
print(Psalm3.find('nikodimos'))

#Examle for string.index()
proverb0 = "As iron sharpens iron, so one man sharpens another."
print(proverb0.index("s"))

#Example for string.startswith()
proverb1 = "Charm is deceptive, and beauty is fleeting; but a woman who fears the Lord is to be praised."
print(proverb1.startswith("C"))

#Example for string.endswith()
print(proverb1.endswith("ed."))

#Example for string.count()
print(proverb1.count("m"))

#Example for string.replace()
text = "--hello world--"
print(text.replace("h","H"))
print(text.replace("o","0",1))

#Example for string.strip()
print(text.strip("-"))

#Example for string.lstrip
print(text.lstrip("-"))

#Example for string.rstrip()
print(text.rstrip("-"))

#Example for string.split()
text1 = 'one two three four five'
print(text1.split())

#Example for string.join()
words = ["The" ,"fear", "of", "the", "Lord", "is" ,"the", "beginning", "of", "wisdom"]
sentence = ' '.join(words)
print(sentence)

#Example for string.isalpha()
print(God.isalpha())
language = "python"
print(language.isalpha())

#Example for string.isdigit()
numbers = "012345678"
print(numbers.isdigit())

# Example for str.isalnum()
text = "abc123"
print(text.isalnum())  

# Example for str.isspace()
space_text = "   \t\n"
print(space_text.isspace()) 

# Example for str.format()
name = "Nikodimos"
print("Hello, {}".format(name)) 

# Example for f-strings
age = 25
print(f"I am {age} years old") 

# Example for len()
message = "Hello"
print(len(message))  

# Example for str.encode()
ethiopic = "ሰላም"
print(ethiopic.encode())
