import random


def main():
    level = int(get_level())
    score = 0
    for i in range(1,11):
        tries = 3
        x = generate_integer(level)
        y = generate_integer(level)
        while tries > 0:
            message = str(x)+" + "+str(y)+" ="
            try:
                sum1 = int(input(message))
                if sum1 == x + y:
                    score = score + 1
                    break
                elif sum1 != x + y:
                    tries = tries - 1
                    print("EEE")
                    continue
            except ValueError:
                tries = tries - 1
                print("EEE")
                continue
        print(message,x+y)
    print("Score:",score)


def get_level():
    while True:
        try:
            level1 = int(input("Level:"))
            if level1 in range(1,4):
                return level1
                break
            else:
                continue
        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        num_random = random.randint(10**(level-1)-1,(10**level)-1)
        return num_random
    else:
        num_random = random.randint(10**(level-1),(10**level)-1)
        return num_random

if __name__ == "__main__":
    main()
