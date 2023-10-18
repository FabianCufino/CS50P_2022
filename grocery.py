def sloop():
    dic_1 = {}
    while True:
        try:
            item = input("").upper()
            if item in list(dic_1):
                value_1 = dic_1.get(item)
                value_2 = value_1 + 1
                dic_1.update({item:value_2})
            else:
                dic_1.update({item:1})
            #print ("Item:",item,"valor",dic_1.get(item))
        except ValueError:
            print("value error item not in list")
        except EOFError:
            dic_2 = dict(sorted(dic_1.items()))
            for i in list(dic_2):
                print(dic_2[i],i)
            #print (dic_2)
            #print("goodbye")
            break

sloop()
