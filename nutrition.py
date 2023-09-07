def main():
    f = input("Item: ").lower().strip()
    result = search(f)
    if result != None:
        print("Calories:",result)




def search(n):
    fruits = {
        "Apple": 130,
        "Avocado": 50,
        "Banana": 110,
        "Cantaloupe": 50,
        "Grapefruit": 60,
        "Grapes": 90,
        "Honeydew Melon": 50,
        "Kiwifruit": 90,
        "Lemon": 15,
        "Lime": 20,
        "Nectarine": 60,
        "Orange": 80,
        "Peach": 60,
        "Pear": 100,
        "Pineapple": 50,
        "Plums": 70,
        "Strawberries": 50,
        "Sweet Cherries": 100,
        "Tangerine": 50,
        "Watermelon": 80
    }

    dict_fruit = {}

    for i in list(fruits):
        fruit_lower = i.lower()
        calories = fruits.get(i)
        dict_fruit.update({fruit_lower:calories})


    if n in list(dict_fruit):
        cl = dict_fruit.get(n)
        return cl
    else:
        return None

main()
