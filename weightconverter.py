w = int(input("Enter your weight:"))
u = str(input("Give unit(kg/g):"))
if u == "kg" :
    w = w*1000
    print("weight in grams is:",w)
else:
    w = w/1000
    print("weight in kg is:",w)