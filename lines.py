import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif sys.argv[1][-3:] != ".py":
    sys.exit("Not a Python file")

try:
    with open(sys.argv[1], "r") as file:
        lines = file.readlines()
except FileNotFoundError:
    sys.exit("File does not exist")

#print(lines)
count = 0
for x in lines:
    if  len(x.strip()) == 0:
        count = count

    elif x.strip()[0] == "#":
        count = count
        #print("v1",x)
    else:
        count = count + 1

print (count)
