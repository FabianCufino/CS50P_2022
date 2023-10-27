import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search(r"^([0-9]+\.){3}[0-9]+$", ip):
        a,b,c,d = ip.split(".")
        #print(a,b,c,d)
        if int(a) >= 256 or int(b) >= 256 or int(c) >= 256 or int(d) >= 256:
            return False
        else:
            return True
    else:
        return False


if __name__ == "__main__":
    main()