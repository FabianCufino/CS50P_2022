import sys

def main():
    in1 = input("Fraction: ")
    frac_1 = convert(in1)
    gau = gauge(frac_1)
    print(gau)

def convert(fraction):
    try:
        x, y = fraction.split("/")
        x1 = int(x)
        y1 = int(y)
        frac = round((x1/y1) * 100)
        if frac > 100:
            raise ValueError
        return int(frac)

    except ValueError:
        raise
        #sys.exit("El valor no puede ser mayor que 1")
    except ZeroDivisionError:
        raise
        sys.exit("no se puede dividir por 0")

def gauge(percentage):

    if percentage <= 1:
        #print ("E")
        return "E"
    elif 99<=percentage <= 100:
        return "F"
    else:
        int1 = int(percentage)
        return f"{int1}%"

if __name__ == "__main__":
    main()
