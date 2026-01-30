a = int(input("Enter the number whose table is required:"))
i=a

print("using for loop")
for i in range(a,a*11,a):
    print(i)

i=a
print("using while loop")
while (i<=10*a):
    print(i)
    i = i+a
