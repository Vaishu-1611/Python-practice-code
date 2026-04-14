s = str(input("Enter the shape (circle,rectangle,square,triangle):"))

if s == "circle":
    r = float(input("Enter the radius of the circle:"))
    a = 3.14 * r * r
    print("The area of the circle is :",a)
elif s == "rectangle":
    l = float(input("Enter length of the rectangle:"))
    b = float(input("Enter breadth of the rectangle:"))
    a = l * b
    print("The area of the rectangle is :",a)
elif s == "square":
    s = float(input("Enter the side of the square:"))
    a = s * s
    print("The area of the square is :",a)
elif s == "triangle":
    b = float(input("Enter the base of the traingle:"))
    h = float(input("Enter the hight of the triangle:"))
    a = 0.5 * b * h
    print("The area of the triangle is :",a)
else:
    print("Invalid shape entered. Please enter a valid shape.")