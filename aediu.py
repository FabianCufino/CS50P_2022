import inflect

p = inflect.engine()

word = "woman"

#print("The plural of ", word, " is ", p.plural(word))



def adieu():
    list_1 = []
    while True:
        try:
            name = input("Name: ")
            list_1.append(name)
            #print("largo es",len(list_1))
        except ValueError:
            print("value error item not in list")
        except EOFError:
            if len(list_1) == 0:
                print("goodbye")
            elif len(list_1) == 1:
                print ("Adieu, adieu, to",list_1[0])
            elif len(list_1) == 2:
                print ("Adieu, adieu, to",list_1[0],"and",list_1[1])
            elif len(list_1) > 2:
                tex_names = ""
                for i in list_1[:-2]:
                    tex_names = tex_names + i + ", "
                #print (name)
                print ("Adieu, adieu, to ", tex_names, list_1[-2],", and ", list_1[-1], sep="")
            break

adieu()
