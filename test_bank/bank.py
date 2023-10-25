def main():
    g =  input("Write yout sentence--> ")
    print(f"${value(g):,}")

def value(greeting):

    greeting_1 = greeting.lower().strip()
    if "hello" in greeting_1[0:5]:
        return 0
    elif "h" == greeting_1[0]:
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()

