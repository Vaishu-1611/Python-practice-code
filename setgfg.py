#creating set

s = {1, 2, 3, 4}
print(s)

s = set()
print(s)

s = set("GeeksForGeeks")
print(s)

# Creating a Set with the use of a List
s = set(["GFG", "For", "Geeks"])
print(s)

# Creating a Set with the use of a tuple
t = ("GFG", "for", "Geeks")
print(set(t))

# Creating a Set with the use of a dictionary
d = {"GFG": 1, "for": 2, "Geeks": 3}
print(set(d))

s = {3, 1, 4, 1, 5, 9, 2}

print(s) 
try:
    print(s[0])
except TypeError as e:
    print(e)

#adding elements to set
s = {1, 2, 3}
s.add(4)
s.update([5, 6])
print(s)

#accessing set elements
s = {"Geeks", "For", "Geeks"}

for i in s:
    print(i, end=" ")

print("\n", "Geeks" in s)

#removing elements from set
s = {1, 2, 3, 4, 5}
s.remove(3) # Removes the element 3 from the set s. If 3 is not present in the set, it raises a KeyError.
print(s)  

try:
    s.remove(10) # Attempting to remove an element that is not present in the set will raise a KeyError
except KeyError as e:
    print("Error:", e)  

s.discard(4) # Removes the element 4 from the set s. If 4 is not present in the set, it does nothing (no error is raised).
print(s)  

s.discard(10)  # Attempting to discard an element that is not present in the set does nothing (no error is raised)
print(s)

s = {1, 2, 3, 4, 5}
val = s.pop() # Removes and returns an arbitrary element from the set s. If the set is empty, it raises a KeyError.
print(val)
print(s)

s.clear()  
try:
    s.pop() # Attempting to pop from an empty set will raise a KeyError
except KeyError as e:
    print("Error:", e)

#typecasting elements to set
li = [1, 2, 3, 3, 4, 5, 5, 6, 2]
s = set(li)
print(s)

s = "GeeksforGeeks"
s = set(s)
print(s)

d = {1: "One", 2: "Two", 3: "Three"}
s = set(d)
print(s)