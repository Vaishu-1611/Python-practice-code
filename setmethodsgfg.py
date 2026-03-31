#adding and removing elements from set
# set of letters
s = {'g', 'e', 'k', 's'}

# adding 's'
s.add('f')
print('Set after updating:', s)

# Discarding element from the set
s.discard('g')
print('\nSet after updating:', s)

# Removing element from the set
s.remove('e')
print('\nSet after updating:', s)

# Popping elements from the set
print('\nPopped element', s.pop())
print('Set after updating:', s)

s.clear()
print('\nSet after updating:', s)

#copying a set
# Python3 program to demonstrate the use
# of join() function 

set1 = {1, 2, 3, 4} 

# function to copy the set
set2 = set1.copy() 

# prints the copied set
print(set2)

# Python program to demonstrate that copy 
# created using set copy is shallow
first = {'g', 'e', 'e', 'k', 's'}
second = first.copy()

# before adding
print ('before adding: ')
print ('first: ',first)
print ('second: ', second )

# Adding element to second, first does not
# change.
second.add('f')

# after adding
print ('after adding: ')
print ('first: ', first)
print ('second: ', second )

A = {10, 20, 30, 40, 80}
B = {100, 30, 80, 40, 60}

print(A.difference(B))  # Elements in A but not in B
print(B.difference(A))  # Elements in B but not in A

A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}
C = {5, 6, 7, 8, 9}

res = A.difference(B, C)  # Elements in A that are not in B or C
print(res)

A = {10, 20, 30, 40}
B = set()
print(A.difference(B))

A = {10, 20, 30, 40, 80}
B = {10, 20, 30, 40, 80, 100}

print(A.difference(B))  # Returns an empty set as A is fully contained in B

# Python code to get the difference between two sets
# using difference_update() between set A and set B

# Driver Code
A = {10, 20, 30, 40, 80}
B = {100, 30, 80, 40, 60}

# Modifies A and returns None
A.difference_update(B)

# Prints the modified set
print (A)

