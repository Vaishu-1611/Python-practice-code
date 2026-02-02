def GD(name,ending):
    print("Good Day! " + name + " " )
    print(ending)

    return "OK"

a = GD("Vaishnavi", "How are you?")
print(a)


def goodday( name, ending = "Thank You" ):
    print(f"Good Day! , { name }" )
    print(ending)

goodday("Ankita")
goodday("Rohit", "How are you?")