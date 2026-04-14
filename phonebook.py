dict ={}
n = int(input("Enter the number of entries in the phonebook:"))
for i in range(n):
    name = input("Enter the name:")
    number = input("Enter the phone number:")
    dict[name] = number

print("The phonebook is:", dict)
search_name = input("Enter the name to search:")
if search_name in dict:
    print("The phone number of", search_name, "is:", dict[search_name])
else:
    print("Name not found in the phonebook.")
