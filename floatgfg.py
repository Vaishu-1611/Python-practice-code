f = 2.75
ratio = f.as_integer_ratio() # Returns a tuple (numerator, denominator) such that f = numerator/denominator
print(ratio)

f = 5.5
print(f.conjugate()) # Returns the complex conjugate of the float. For a real number, this is just the number itself.

s = "0x1.91eb851eb851fp+1"
a = float.fromhex(s) # Converts a hexadecimal string to a float. The string must be in the format [sign]0x1.[hex_digits]p[exponent]
print(a)

f = 3.14
print(f.hex()) # Converts a float to a hexadecimal string. The result is a string in the format [sign]0x1.[hex_digits]p[exponent]

print((4.0).is_integer()) # Returns True because 4.0 is an integer value, even though it's a float.
print((4.5).is_integer()) # Returns False because 4.5 is not an integer, even though it's a float.

f = -7.3
print(f.__abs__()) # Returns the absolute value of the float. This is the same as abs(f) but can be called as a method. 
print(abs(f)) # Returns the absolute value of the float. This is the same as f.__abs__() but is more commonly used.

a = 5.5
b = 2.2
print(a.__add__(b)) #adds 2 float numbers
print(a + b) # Returns the sum of a and b. This is the same as a.__add__(b) but is more commonly used.

a = 10.5
b = 3.2
print(a.__sub__(b))  
print(a - b) # Returns the difference of a and b. This is the same as a.__sub__(b) but is more commonly used.

a = 4.2
b = 2.0
print(a.__mul__(b))   
print(a * b) # Returns the product of a and b. This is the same as a.__mul__(b) but is more commonly used.

a = 7.5
b = 2.5
print(a.__truediv__(b))   
print(a / b) # Returns the quotient of a and b. This is the same as a.__truediv__(b) but is more commonly used.

a = 7.5
b = 2.5
print(a.__floordiv__(b))   
print(a // b) # Returns the floor division of a by b. This is the same as a.__floordiv__(b) but is more commonly used.

a = 10.5
b = 4.0
print(a.__mod__(b))   
print(a % b) # Returns the modulus of a by b. This is the same as a.__mod__(b) but is more commonly used.

a = 3.0
b = 2.0
print(a.__pow__(b))   
print(a ** b) # Returns a raised to the power of b. This is the same as a.__pow__(b) but is more commonly used.

f = 3.14159
print(f.__round__(2))  
print(round(f, 2)) # Rounds the float to 2 decimal places. This is the same as f.__round__(2) but is more commonly used.
print(f.__round__(3))
print(round(f, 3)) # Rounds the float to 3 decimal places. This is the same as f.__round__(3) but is more commonly used.