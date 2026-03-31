#creating a dictionary
a = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(a)

b = dict(a = "Geeks", b = "for", c = "Geeks")
print(b)

#accessing dictionary elements
d = { "name": "Kat", 1: "Python", (1, 2): [1,2,4] }

# Access using key
print(d["name"])

# Access using get()
print(d.get("name"))

d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}

# Adding a new key-value pair
d["age"] = 22

# Updating an existing value
d[1] = "Python dict"
print(d)

#deleting dictionary elements
d = {1: 'Geeks', 2: 'For', 3: 'Geeks', 'age':22}

# Using del 
del d["age"]
print(d)

# Using pop() 
val = d.pop(1)
print(val)

# Using popitem()
key, val = d.popitem()
print(f"Key: {key}, Value: {val}")

# Using clear()
d.clear()
print(d)

#iterating through a dictionary
d = {1: 'Geeks', 2: 'For', 'age':22}

# Iterate over keys
for key in d:
    print(key)

# Iterate over values
for value in d.values():
    print(value)

# Iterate over key-value pairs
for key, value in d.items():
    print(f"{key}: {value}")

#nested dictionaries
d = {1: 'Geeks', 2: 'For', 3: {'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}}
print(d)

