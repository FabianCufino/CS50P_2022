def greetings():
    g =  input("Write yout sentence--> ").lower().strip()
    print(pay(g))

def pay(n1):
    if n1.startswith("hello"):
        n2="$0"
    elif n1.startswith("how you doing"):
        n2="$20"
    elif n1.startswith("hi"):
        n2= "$20"
    else:
        n2="$100"
    return n2

greetings()
