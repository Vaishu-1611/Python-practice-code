#list creation
a = [1, 2, 3, 4, 5] # List of integers
b = ['apple', 'banana', 'cherry'] # List of strings
c = [1, 'hello', 3.14, True] # Mixed data types

print(a)
print(b)
print(c)

#using list constructor
a = list((1, 2, 3, 'apple', 4.5))  
print(a)

b = list("GFG")
print(b)

a = [2] * 5
b = [0] * 7
print(a)
print(b)

a = [10, 20, "GfG", 40, True]
print(a)        
print(a[0])     
print(a[1])  
print(a[2])

#list accessiing elements
a = [10, 20, 30, 40, 50]
print(a[0])    
print(a[-1])
print(a[1:4])   # elements from index 1 to 3

#add elements to list
a = []

a.append(10) # Appends 10 to the end of the list a. The list becomes [10].
print("After append(10):", a)  

a.insert(0, 5) # Inserts 5 at index 0 in the list a. The list becomes [5, 10].
print("After insert(0, 5):", a) 

a.extend([15, 20, 25]) # Extends the list a by appending elements from the iterable [15, 20, 25]. The list becomes [5, 10, 15, 20, 25].
print("After extend([15, 20, 25]):", a) 

a.clear() # Removes all elements from the list a. The list becomes an empty list [].
print("After clear():", a)

#list updating
a = [10, 20, 30, 40, 50]
a[1] = 25 
print(a)

#removing elements from list
a = [10, 20, 30, 40, 50]

a.remove(30)  # Removes the first occurrence of the value 30 from the list a. The list becomes [10, 20, 40, 50]. 
print("After remove(30):", a)

popped_val = a.pop(1)  # Removes and returns the element at index 1 from the list a. The list becomes [10, 40, 50], and popped_val is assigned the value 20.
print("Popped element:", popped_val)
print("After pop(1):", a) 

del a[0]  # Deletes the element at index 0 from the list a. The list becomes [40, 50].
print("After del a[0]:", a)

#list iteration
a = ['apple', 'banana', 'cherry']
for item in a:
    print(item)

#nested list
matrix = [ [1, 2, 3],
           [4, 5, 6],
           [7, 8, 9] ]
print(matrix[1][2])

#list comprehension
squares = [x**2 for x in range(1, 6)]
print(squares)





