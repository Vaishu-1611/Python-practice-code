animals = frozenset(["cat", "dog", "lion"])
print("cat" in animals) 
print("elephant" in animals)

# passing an empty tuple
nu = ()

# converting tuple to frozenset
fnum = frozenset(nu)

# printing empty frozenset object
print("frozenset Object is : ", fnum)

l = ["Geeks", "for", "Geeks"]
 
# converting list to frozenset
fnum = frozenset(l)
 
# printing empty frozenset object
print("frozenset Object is : ", fnum)

# creating a dictionary 
Student = {"name": "Ankit", "age": 21, "sex": "Male", 
           "college": "MNNIT Allahabad", "address": "Allahabad"}

# making keys of dictionary as frozenset
key = frozenset(Student)

# printing dict keys as frozenset
print('The frozen set is:', key)

# initialize A and B
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])

# copying a frozenset
C = A.copy()
print(C)  

# union
union_set = A.union(B)
print(union_set) 

# intersection
intersection_set = A.intersection(B)
print(intersection_set)  

difference_set = A.difference(B)
print(difference_set) 

# symmetric_difference
symmetric_difference_set = A.symmetric_difference(B)
print(symmetric_difference_set)

fruits = frozenset(["apple", "banana", "orange"])
print(fruits) 
'''fruits.add("cherry")
print(fruits)''' #creates error as frozenset does not support add() method

# creating a list 
favourite_subject = ["OS", "DBMS", "Algo"]

# creating a frozenset
f_subject = frozenset(favourite_subject)

# below line will generate error
'''f_subject[1] = "Networking"''' #creates error as frozenset does not support item assignment

s1 = {1, 2, 3}
s2 = {2, 3}
print(s1.intersection(s2))

# Python3 program for intersection() function
set1 = {2, 4, 5, 6}
set2 = {4, 6, 7, 8}
set3 = {4, 6, 8}

# intersection of two sets
print("set1 intersection set2 : ",
      set1.intersection(set2))

# intersection of three sets
print("set1 intersection set2 intersection set3 :",
      set1.intersection(set2, set3))

# Python3 program for intersection() function
set1 = {2, 4, 5, 6}
set2 = {4, 6, 7, 8}
set3 = {1, 0, 12}

print(set1 & set2)
print(set1 & set3)

print(set1 & set2 & set3)

# Python3 program for intersection() function
set1 = {2, 4, 5, 6}
set2 = {4, 6, 7, 8}
set3 = {1, 0, 12}

print(set1.symmetric_difference(set2))
print(set1.symmetric_difference(set3))
print(set2.symmetric_difference(set3))

set1 = {}
set2 = {}

# union of two sets
print("set1 intersection set2 : ",
      set(set1).intersection(set(set2)))

s1 = {1, 2, 3}
s2 = {4, 5, 6}
print(s1.isdisjoint(s2))

# Python3 program for isdisjoint() function
set1 = {2, 4, 5, 6}
set2 = {7, 8, 9, 10}
set3 = {1, 2}

# checking of disjoint of two sets
print("set1 and set2 are disjoint?",
      set1.isdisjoint(set2))

print("set1 and set3 are disjoint?",
      set1.isdisjoint(set3))

# Set
A = {2, 4, 5, 6}

# List
lis = [1, 2, 3, 4, 5]

# Dictionary dict, Set is formed on Keys
dict = {1: 'Apple', 2: 'Orange'}

# Dictionary dict2
dict2 = {'Apple': 1, 'Orange': 2}

print("Set A and List lis disjoint?", A.isdisjoint(lis))
print("Set A and dict are disjoint?", A.isdisjoint(dict))
print("Set A and dict2 are disjoint?", A.isdisjoint(dict2))

# Python code to demonstrate
# isdisjoint method with blank
# sets

# defining empty set1
s1 = set()

# defining empty set2
s2 = set()


# using the isdisjoint method 
# with empty sets
print(s1.isdisjoint(s2))

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5}
print(s2.issubset(s1))

A = {4, 1, 3, 5}
B = {6, 0, 4, 1, 5, 0, 3, 5}

print(A.issubset(B))
print(B.issubset(A))
A = {4, 1, 3, 5}
B = {6, 0, 4, 1, 5, 0, 3, 5}

print(A.issubset(B))
print(B.issubset(A))

A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {1, 2, 4, 5}

print(A.issubset(B))
print(B.issubset(A))


print(A.issubset(C))
print(C.issubset(B))

A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {1, 2, 4, 5}

print("A.issuperset(B) : ", A.issuperset(B))
print("B.issuperset(A) : ", B.issuperset(A))
print("A.issuperset(C) : ", A.issuperset(C))
print("C.issuperset(B) : ", C.issuperset(B))

# Python program to demonstrate the use of 
# of symmetric_difference() method 


list1 = [1, 2, 3] 
list2 = [2, 3, 4] 
list3 = [3, 4, 5] 

# Convert list to sets
set1 = set(list1) 
set2 = set(list2) 

# Prints the symmetric difference when  
# set is passed as a parameter 
print(set1.symmetric_difference(set2)) 

# Prints the symmetric difference when list is 
# passed as a parameter by converting it to a set
print(set2.symmetric_difference(list3))

# Python code to demonstrate working of
# symmetric_difference_update()

A = {'p', 'a', 'w', 'a', 'n'}
B = {'r', 'a', 'o', 'n', 'e'}

# result is always none.
result = A.symmetric_difference_update(B)

print('A = ', A)
print('B = ', B)
print('result = ', result)

# Python code to demonstrate working of
# symmetric_difference_update()

A = {'s', 'u', 'n', 'n', 'y'}
B = {'b', 'u', 'n', 'n', 'y'}

# result is always none.
result = A.symmetric_difference_update(B)

print('A = ', A)
print('B = ', B)
print('result = ', result)

# Python code to demonstrate working of
# symmetric_difference_update()

A = {1, 2, 3, 4, 5, 6}
B = [4, 5, 7, 8]

# passing argument as list

A.symmetric_difference_update(B)
print("A =", A)

A = {2, 4, 6, 8}
B = (i for i in range(2, 6))

# passing argument as generator object

A.symmetric_difference_update(B)
print("A=", A)

# Python code to demonstrate working of
# symmetric_difference_update()

A = {1, 2, 3, 4, 5}
B = [[1, 2, 3], 4, 5]

'''error as b contain one element as list(unhashable object)
A.symmetric_difference_update(B) 
print("A =", A)'''

A = {1, 2, 3} 
B = {3, 4, 5}
print(A.union(B))  # Combining both sets

A = {2, 4, 5, 6}
B = {4, 6, 7, 8}
C = {7, 8, 9, 10}

# using multiple union calls
print("A U B U C:", A.union(B).union(C))

# directly passing multiple sets
print("A U B U C:", A.union(B, C))

A = {2, 4, 5, 6}
B = {4, 6, 7, 8}
C = {7, 8, 9, 10}

# Using | operator for union
print("A U B:", A | B)
print("A U B U C:", A | B | C)

A = {'ab', 'ba', 'cd', 'dz'} 
B = {'cd', 'ab', 'dd', 'za'}
print("A U B:", A.union(B))

s = {1, 2, 3}
s.update([3, 4, 5])
print(s)

d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
d1.update(d2)
print(d1)

d1 = {'a': 1, 'b': 2}
d1.update([('c', 3), ('d', 4)])
print(d1)

d1 = {'a': 1, 'b': 2}
d1.update(c=3, d=4)
print(d1)

s1 = {1, 2, 3}
s1.update("hello")
print(s1)

s1 = {1, 2, 3, 4}
print("Before popping: ",s1)
s1.pop()
s1.pop()
s1.pop()
print("After 3 elements popped, s1:", s1)

S = {}

'''popping an element
print(S.pop())
print("Updated set is", S)'''