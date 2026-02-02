def sum(n):

    if (n>=1):
        s = n + sum(n-1)
        return s
    else:
        return 0

n = int(input("Enter a natural number: "))    
sum(n)
print("The sum of first", n, "natural numbers is:", sum(n))