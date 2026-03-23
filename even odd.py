a = int(input('Enter a number: '))
if a % 2 == 0:
    print('even number')
else:
    print('odd number')


n = int(input('enter a number: '))
i = 0
for i in range (n):
    print(i )
    i = i+1

sum = 0
n = int(input('enter a number: '))
for i in range (n+1):
    sum = sum + i   #sum of first n numbers
print('the sum of first',n,'numbers is',sum)

#sum of digits of a number
remainder = 0
total = 0
x = int(input('enter a number: '))
while x !=0:
    remainder = x % 10
    total = total + remainder
    x= x // 10
print('the sum of digits is',total)


#reverse of a number
remainder = 0
reverse = 0
x = int(input('enter a number: '))
while x !=0:
    remainder = x % 10
    reverse = reverse * 10 + remainder
    x= x // 10
print('the reverse of the number is',reverse)


