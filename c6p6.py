print("Enter your marks outof 100")
a = int(input("Enter marks of subject 1:"))
b = int(input("Enter marks of subject 2:"))
c = int(input("Enter marks of subject 3:"))

total = (a+b+c)/3

if (90< total <=100):
    grade = 'Ex'
elif(80 < total <=90):
    grade = 'A'
elif(70 < total <=80):
    grade = 'B'
elif(60 < total <=70):
    grade = 'C'
elif(50 < total <=60):
    grade = 'D'
else:
    grade = 'F'

print("Your grade is:",grade)
    