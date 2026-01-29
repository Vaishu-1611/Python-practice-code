c = {} #empty dictionary
print(type(c))
a = {
    "harry": 88,
    "vaishnavi":97,
    "palak":90,
    "key":"value",
    "list":[1,2,9]
}
print(a,type(a))
print(a["harry"])
print(a.get("harry"))
#print(a["harry2"]) #returns error
print(a.get("harry2")) #prints none
print(a["key"])
print(a["list"])
print(a.items())
print(a.keys())
print(a.values())
a.update({"palak":86,"vaishali":91})
print(a)
a.pop("key")
print(a)
b = a.popitem()
print(b)
print(a)
a.clear()
print(a)


