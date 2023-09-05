def main():
    in1 = input("What time is it? ")
    time = convert(in1)

    if 7 <= time <= 8:
        meal = "breakfast time"
    elif 12 <= time <= 13:
        meal = "lunch time"
    elif 18 <= time <= 19:
        meal = "dinner time"
    else:
        meal = ""

    print (meal)


def convert(time):
    hour, minute = time.split(":")
    time_fix = float(hour) + float(minute) /60
    return time_fix


if __name__ == "__main__":
    main()
