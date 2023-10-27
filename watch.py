import re
import sys


def main():
    print(parse(input("HTML: ")))

def parse(s):
    matches1 = re.search(r'.+src=["]([^"]+)["].*$', s)
    if matches1:
        url = matches1.groups(1)[0]
        #print(url)
        matches2 = re.search(r'^https?://w?w?w?\.?youtube.com/embed/([a-zA-Z0-9_]+)$', url)
        if matches2:
            url2 = matches2.groups(1)[0]
            #print(url2)
            return "https://youtu.be/" + url2
        else:
            return None
    else:
        return None


if __name__ == "__main__":
    main()


