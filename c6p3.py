p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

messege = input("enter your comment here:")

if (p1 in messege or p2 in messege or p3 in messege or p4 in messege):
    print("your comment is a spam")
else:
    print("your comment if not a spam")