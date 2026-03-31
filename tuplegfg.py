#creating a tuple
tup = ()
print(tup)

# Using String
tup = ('Geeks', 'For')
print(tup)

# Using List
li = [1, 2, 4, 5, 6]
print(tuple(li))

# Using Built-in Function
tup = tuple('Geeks')
print(tup)

tup = (5, 'Welcome', 7.5, True, [1, 2, 3], {'key': 'value'})
print(tup)

#accessing tuple elements
tup = tuple("Geeks")
print(tup[0])
print(tup[1:4])  
print(tup[:3])

# Tuple unpacking
tup = ("Geeks", "For", "Geeks")

# This line unpack values of Tuple1
a, b, c = tup
print(a)
print(b)
print(c)

#concatination of tuples
tup1 = (0, 1, 2, 3)
tup2 = ('Geeks', 'For', 'Geeks')
tup3 = tup1 + tup2
print(tup3)

#slicing of tuples
tup = tuple('GEEKSFORGEEKS')
print(tup[1:])
print(tup[::-1])
print(tup[4:9])

tup = (1, 2, 3, 4, 5)
a, *b, c = tup # Unpacking the tuple into variables a, b, and c. a gets the first element (1), c gets the last element (5), and b gets the remaining elements as a list [2, 3, 4].
print(a) 
print(b) 
print(c)

#deleting a tuple
tup = (0, 1, 2, 3, 4)
del tup
print(tup)