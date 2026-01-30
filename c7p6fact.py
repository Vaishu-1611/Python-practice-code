n = int(input("Enter a number:"))

fact=1

i=1
for i in range (1,n+1):
    fact=fact*i
    if(i==n):
        print("factorial of all natural numbers n is :",fact)
    i+=1
    