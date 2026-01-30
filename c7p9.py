n = int(input("enter number of line:"))

for i in range (0,n):
    if i==0:
        print("*"*n,end="")
        print("\n")
    elif i == n-1:                                   
        print("*"*n,end="")
        print("\n")
    else:
        print("*"," "*(n-3),end="*")
        print("\n")

'''***
   * *
   ***'''
'''
or
n = int(input("enter number of line:"))
for i in range(1,n+1):
    if (i==1 or 1==n):
        print(("*)*n,end="")
    else:
        print("*",end="")
        print(" "*(n-2),end="")
        print("*",end="")
    print("\n")'''