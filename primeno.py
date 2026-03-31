n = int(input('enter a number:'))

if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print('the given number is not a prime number')
            break
        else:
            print('the given number is a prime number')
            break
else:
    print('the given number is not a prime number')

s = int(input('enter a starting number:'))
e = int(input('enter an ending number:'))
print('the prime numbers between',s,'and',e,'are:')
for num in range(s,e+1):
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                break
        else:
            print(num)