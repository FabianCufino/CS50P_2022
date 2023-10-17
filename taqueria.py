def search(n):
    prices_raw = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    prices = {}

    for i in list(prices_raw):
        item_lower = i.lower()
        price_x1 = prices_raw.get(i)
        prices.update({item_lower:price_x1})


    if n in list(prices):
        cl = prices.get(n)
        return cl
    else:
        return False


def sloop():
    cost = 0
    while True:
        try:
            price_item = float(search(input("Item: ").lower()))
            if price_item > 0:
                 cost = cost + price_item
                 print ("Total:",'${:,.2f}'.format(cost))

        except ValueError:
            print("value error item not in list")
        except EOFError:
            #print("goodbye")
            break

sloop()
