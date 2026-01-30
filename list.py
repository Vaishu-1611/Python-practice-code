l1 = [1, 8, 7, 2, 21, 15] #list is mutable/changable
print(l1)
print(l1[2]) #accessing 3rd element
l1[3] = 17 #changing 4th element
print(l1)
l1.sort() #sorts the list
print(l1) 
l1.reverse() #reverses the list
print(l1) 
l1.append(45) #adds 45 to the end of the list
print(l1) 
l1.insert(2, 11) #inserts 11 at index 2
print(l1) 
l1.remove(21) #removes 21 from the list
print(l1) 
print(l1.pop()) #removes last element and returns its value
print(l1) 
print(l1.index(8)) #returns the index of 8
print(l1.count(7)) #returns the count/number of 7
l2 = [3, 6, 9] 
l1.extend(l2) #adds l2 elements to l1 at the end
print(l1) 
l1.clear() #removes all elements from the list
print(l1) 

