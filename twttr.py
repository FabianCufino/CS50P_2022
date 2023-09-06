def main():
    name = input("Input: ")
    lis = list_not_vowel(name)
    text = list_to_string(lis)
    print ("Output:",text)



def list_not_vowel(n):
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
    return n1

def list_to_string(s):

    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

    # return string
    return str1

main()
