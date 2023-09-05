x = input("Write your input--> ").lower().strip()
match x:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")
