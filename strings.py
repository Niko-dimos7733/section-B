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