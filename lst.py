l = list(map(int, input("Enter the numbers:").split()))
print("the list is:",l)
print("the maximum number is:",max(l))
print("the minimum number is:",min(l))
l.sort()
print("the sorted list is:",l)
print("the maximun number is:",l[-1])
print("the minimum number is:",l[0])
print("the second largest number is:",l[-2])
print("the second smallest number is:",l[1])

print("even numbers in the list are:")
for i in range(len(l)):
    if l[i] % 2 == 0:
        print(l[i])
print("odd numbers in the list are:")
for i in range(len(l)):
    if l[i] % 2 != 0:
        print(l[i])

sum=0
for items in l:
    sum += items
print("the sum of numbers in list is:",sum)

print("list after removing duplicates is:",list(set(l)))

freq = {}
for item in l:
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1

print("frequency of each number is:",freq)

print("the reverse of the list is :",l[::-1])
