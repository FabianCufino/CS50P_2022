def main():
    name = input("Input: ")
    text = shorten(name)
    print ("Output:",text)

def shorten(n):
    vowels = ["a","e","i","o","u"]
    n1 = []
    i = 0
    while i < len(n):
        x = n[i:i+1]
        if x.lower() in vowels:
            v = 1
        else:
            n1.extend(x)
        i += 1
    str1 = ""
    for ele in n1:
        str1 += ele

    return str1

if __name__ == "__main__":
    main()