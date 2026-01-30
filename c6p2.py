print("Enter marks outof 100")
a = int(input("Enter marks of subject 1:"))
b = int(input("Enter marks of subject 2:"))
c = int(input("Enter marks of subject 3:"))

total = (a+b+c)/3

if (a>=33 and b>=33 and c>=33 and total>=40):
    print("Student has passed his/her examination:",total)
else:
    print("Student has failed his/her examination:",total)
    