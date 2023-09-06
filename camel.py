name_in = input("camelcase--> ")
wlist = []

for c in range(len(name_in)):
    c1 = name_in[c:c+1]
    if c1.isupper():
        wlist.append(c)
        #print("letra ", c1 , "es mayuscula",c)
    else:
        continue

if wlist.count(0) == 0:
    wlist.insert(0,0)
#print(wlist)

if len(wlist) == 1:
    new_word = name_in.lower()
else:
    i = 0
    while i < len(wlist):
        if i == 0:
            new_word = name_in[wlist[0]:wlist[i+1]].lower()
        elif i == len(wlist)-1:
            new_word = new_word + "_" + name_in[wlist[i]:].lower()
        else:
            new_word = new_word + "_" + name_in[wlist[i]:wlist[i+1]].lower()
        i += 1
#print ("snake_case: ",new_word)
print (new_word)
