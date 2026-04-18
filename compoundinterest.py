p = 0
t = 0
r = 0

while p <= 0 :
    p = float(input("Enter the principle amount:"))
    if p <= 0:
        print("principle can't be less than or equal to 0")

while t <= 0 :
    t = float(input("Enter the time amount:"))
    if t <= 0:
        print("time can't be less than or equal to 0")

while r <= 0 :
    r = float(input("Enter the rate amount:"))
    if r <= 0:
        print("rate can't be less than or equal to 0")

a = p * pow((1+r/100),t)
print(f"balance after {t} year/s is: {a:2f} Rs")