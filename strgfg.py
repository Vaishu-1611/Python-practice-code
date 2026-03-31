s1 = 'GfG'  
s2 = "GfG"  
print(s1)
print(s2) 

#multi line string
s = """I am Learning
Python String on GeeksforGeeks"""
print(s)

s = '''I'm a 
Geek'''
print(s) 

#string accessing characters
s = "GeeksforGeeks"
print(s[0])   
print(s[4])

s = "GeeksforGeeks"
print(s[-10])  
print(s[-5])

#string slicing
s = "GeeksforGeeks"
print(s[1:4])    
print(s[:3])     
print(s[3:])    
print(s[::-1])

#string iteration
s = "Python"
for char in s:
    print(char)

#string updating
s = "hello geeks"
s1 = "H" + s[1:]                  
s2 = s.replace("geeks", "GeeksforGeeks")  
print(s1)
print(s2)

#length of string
s = "GeeksforGeeks"
print(len(s))

s = "Hello World"
print(s.upper()) # Converts all characters in the string to uppercase.
print(s.lower()) # Converts all characters in the string to lowercase.
print(s.title()) # Converts the first character of each word to uppercase and the rest to lowercase

s = "   Gfg   "
print(s.strip()) # Removes leading and trailing whitespace from the string. In this case, it removes the spaces before and after "Gfg".

s = "Python is fun"
print(s.replace("fun", "awesome")) # Replaces all occurrences of the substring "fun" with "awesome". The result is "Python is awesome".

#string concatenation
s1 = "Hello"
s2 = "World"
print(s1 + " " + s2)

s = "Hello "
print(s * 3)

#string formatting
name = "Jake"
age = 22
print(f"Name: {name}, Age: {age}")

s = "My name is {} and I am {} years old.".format( "Emily", 22)
print(s)

#string membership
s = "GeeksforGeeks"
print("Geeks" in s)
print("GfG" in s)

#string comparison
s1 = "apple"
s2 = "banana"

print(s1 == s2)
print(s1 != s2)
print(s1 < s2)

#case sensitivity
s1 = "Apple"
s2 = "apple"

print(s1.lower() == s2.lower())

#starting and ending
s = "hello world"

print(s.startswith("hello"))
print(s.endswith("world"))