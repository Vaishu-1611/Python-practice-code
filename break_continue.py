print("break statement")
for i in range (100):
    if (i==30):
        break #exits the loop when i=30
    print(i)

print("continue statement")
for i in range (100):
    if (i == 30):
        continue #skips 30 and continues to print
    print(i)

for i in range (10):
    pass #convi. statement if you want this work on this later

i=0
while (i<10):
    print(i)
    i+=1