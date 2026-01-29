sets = set() #empty set
print(type(sets))
print(sets)
s2 = {} #this is dictionary not set
print(s2)
print(type(s2)) #gives type of s2(dictionary)
s = {1,2,2,3,4,4,5,"harry",54} #do no maintain order, unique items(prints each element once do not consider duplicates)
print(s)
print(type(s)) #gives type of s(set)
s.add(7)
print(s)
s.remove(3) #if element not found gives error
print(s)
s.discard(10) #if element not found does not give error
print(s)
s.discard(7) #if element is found removes it
print(s)
print(len(s)) #number of elements in set
s.pop() #removes random element
print(s)
s2 = {1,2,3,4,5,6} 
print(s.union(s2)) #union of two sets
print(s-s2) #elements in s but not in s2
print(s2-s) #elements in s2 but not in s
print(s.union({8,9,10,4})) #union of two sets
print(s.intersection({54,10})) #common elements in both sets
print(s)
print({2,54}.issubset(s))
print({2,66}.issubset(s)) #checks if all elements of given set are in s
print(s.isdisjoint({2,200})) #no common elements
print(s.isdisjoint({100,200})) #no common elements
print({s.issuperset({2,54})}) #s has all elements of given set
print({s.issuperset({2,66})}) #s has all elements of given set
s.pop() #removes random element
print(s)
s.clear() #removes all elements from set
print(s)
print(len(s))


