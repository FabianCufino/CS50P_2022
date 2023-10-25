def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    secuence = []
    i = 0
    while i < len(s):
        x = s[i:i+1]
        if x.isalpha():
            secuence.extend("a")
        elif x.isnumeric():
            secuence.extend("n")
        else:
            secuence.extend("p")
        i += 1
    #print(secuence)


    if secuence.count("p") == 0:
        if 2<=len(s)<=6:
            if secuence[0] == "a" and secuence[1] == "a":
                if secuence.count("n")> 0:
                    first_digit = secuence.index("n")
                    if secuence.index("n") >= 2 and s[first_digit:first_digit+1] != "0":
                        secuence_r = secuence.copy()
                        secuence_r.reverse()
                        index_last_a =len(s) - secuence_r.index("a")
                        index_first_n =secuence.index("n") + 1
                        if index_last_a < index_first_n:
                            #print("OK, with numerics positions")
                            return True
                        else:
                            #print("contain numbers, but an alphabetical is last")
                            return False
                    else:
                        #print("numerics in first 2 positions or first is 0")
                        return False
                else:
                    #print("corret without numeric positions")
                    return True
            else:
                #print("first 2 positions are not alphabetical")
                return False
        else:
            #print("length is not between 2 - 6")
            return False
    else:
        #print("contain especial characteres")
        return False

if __name__ == "__main__":
    main()