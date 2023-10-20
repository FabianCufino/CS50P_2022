import random
import sys

def main():
    num1 = int(val_num())
    num_guess = random.randint(0, num1)
    while True:
        try:
            try_num = int(input("Guess: "))
            if try_num > num1:
                print("Too large!")
                continue
            elif try_num == num_guess:
                print("Just right!")
                sys.exit()
                break
            elif try_num > num_guess:
                print("Too large!")
                continue
            elif try_num < num_guess:
                print("Too small!")
                continue
        except ValueError:
            continue

def val_num():
    while True:
        try:
            num = input("Level: ")
            if int(num) >= 0:
                return int(num)
                break
        except ValueError:
            continue

main()

