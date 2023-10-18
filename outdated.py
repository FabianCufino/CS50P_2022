def main():
    x = date_correct()

def date_correct():
    months_list = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    dic_months ={}
    for i in range(len(months_list)):
            item_1 = months_list[i]
            dic_months.update({item_1:i+1})

    month_numeric= []
    for i in range(12):
        month_numeric.append(i+1)
    day_numeric = []
    for i in range(31):
        day_numeric.append(i+1)
    #print(month_numeric)

    while True:
        try:
            x = input("Date: ").title().strip()
            if len(x.split(" ")) > 2 and x.count(",")==0: #and x[0].isalpha():
                pass
            elif x.count("/")==2 and x[0].isnumeric():
                split1 = x.split("/")
                day = int(split1[1])
                month = int(split1[0])
                year = int(split1[2])
                #valida si el primer elemnto esta en la liste de meses
                month_numeric.index(month)
                #print("valida mes")
                #valida dia < 31
                day_numeric.index(day)
                #print("valida dia")
                #print("termina ejecucion")
                print(year,f"{month:02}",f"{day:02}",sep="-")
                break
            elif x.count(",")==1 and x[0].isalpha():
                split2 = x.split(",")
                year = int(split2[1])
                split3 = split2[0].split(" ")
                #valida dia
                day = int(split3[1])
                day_numeric.index(day)
                #valida mes
                month = dic_months.get(split3[0])
                months_list.index(split3[0])
                print(year,f"{month:02}",f"{day:02}",sep="-")
                break
            else:
                pass
        except ValueError:
            pass
            #print("error")

main()
