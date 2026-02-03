def rem(l,word):
    for item in l:
            l.remove(word)
            return l
l = ["harry","vaishnavi","vibhanshu","mhetre","soham","sakshi","ankit"]
print(l)
print(rem(l,"vaishnavi"))