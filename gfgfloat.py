a = 10.5  # Float declaration
b = -3.14 # Negative float
c = 2.0   # Even if it looks like an integer, it's a float
d = 1.23e4  # Scientific notation (1.23 × 10⁴ = 12300.0)
e = 5e-3   # Scientific notation (5 × 10⁻³ = 0.005)
print(a,b,c,d,e)

f = 2.75
ratio = f.as_integer_ratio() # Returns a tuple (numerator, denominator) such that f = numerator/denominator
print(ratio)

s = "0x1.91eb851eb851fp+1"
a = float.fromhex(s) # Converts a hexadecimal string to a float. The string must be in the format [sign]0x1.[hex_digits]p[exponent]
print(a)

f = 3.14
print(f.hex()) # Converts a float to a hexadecimal string. The result is a string in the format [sign]0x1.[hex_digits]p[exponent]

print((4.0).is_integer())  
print((4.5).is_integer())

