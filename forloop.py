i = 0

print("Numbers from 0-10 can be written as:")
for i in range (11): #for loop for printing number
    print (i)
print("name in the list are:")
l1 = ['harry',"vaishnavi","rohan","sakshi","vibhanshu","tanmay","kunal","priya","sai","sneha","kumar","anna","biru","polu","simba","chameli","chotu","bhaiya","palak"]
for i in l1: #for loop for list
    print(i)
print("table of 4 an be written as:")
for i in range (0,100,4): # for loop for step printing
    print(i)
print("for tuples")
t = (97,2,3,4,11)
for i in t: # for loop for tuples
    print(i)
print("for string")
s="vaishnavi"
for i in s: #for loop for string
    print(i) 
l = [1,5,9]
for item in l: 
    print(item) #prints all items in list
else:
    print("done") #prints when items in list get over
