in1 = input("write your expresion--> ")
x, y, z = in1.split(" ")
x1 = float(x)
z1 = float(z)

if y == "+":
    result = x1+z1
elif y=="-":
    result = x1-z1
elif y=="*":
    result = x1*z1
elif y=="/":
    result = x1/z1

print(result)
