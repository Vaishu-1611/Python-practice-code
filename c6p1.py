print("Enter 4 different numbers")
a = int (input("Enter no 1:"))
b = int (input("Enter no 2:"))
c = int (input("Enter no 3:"))
d = int (input("Enter no 4:"))

if (a>b and a>c and a>d):
    print("The gratest number is:",a)
elif(b>a and b>c and b>d):
    print("The gratest number is:",b)
elif(c>a and c>b and c>d):
    print("The gratest number is:",c)
else:
    print("The gratest number is:",d)


