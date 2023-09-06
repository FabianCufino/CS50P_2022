cost = 50
#print ("Amount Due is:", cost)
coins_accepted = [25,10,5]
amount_due = cost
while amount_due > 0:
    coin = int(input("Insert Coin: "))
    if coins_accepted.count(coin) == 0:
        print ("Amount Due:", amount_due)
    else:
        amount_due = amount_due-coin
        if amount_due <= 0:
            print ("Change Owed:", -amount_due)
        else:
            print ("Amount Due:", amount_due)



