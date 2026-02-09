f = open("file.txt")
#prints the same content
'''data=f.read()
print(data)

#prints lines in the form of tuples and gives its class
lines = f.readlines()
print(lines , type(lines))

#prints each line seperately

line1 = f.readline()
print(line1 , type(line1))
line2 = f.readline()
print(line2 , type(line2))
line3 = f.readline()
print(line3 , type(line3))
line4 = f.readline()
print(line4 , type(line4))
line5 = f.readline()
print(line5 , type(line5))
line6 = f.readline()
print(line5 == "")'''

#reads files till the last line
line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()
f.close