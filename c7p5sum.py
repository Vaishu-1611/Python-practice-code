n = int(input("Enter a number:"))

i=0
sum=0

for i in range (1,n+1):
    sum=sum+i
    if(i==n):
        print("sum of all natural numbers n is :",sum)
    i+=1    