from os import name
from pprint import pprint
with open ("recipes.txt", "r", encoding="utf-8") as file:
    cook_book = {}
    for line in file:
        dish = line.strip()
        # print(dish)
        cook_book[dish] = []
        ingredients = int(file.readline().strip())
        # print(ingredients)
        for i in range(ingredients):
            str = file.readline().strip()
            str_sp = str.split(" | ")
            # print(str_sp)
            cook_book[dish].append({'ingredient_name': str_sp[0], 'quantity': str_sp[1], 'measure': str_sp[2]})
        file.readline()
        print()
    
# pprint(cook_book)

def get_shoy_dishes(dic, dish, persons):
    cook = {}
    for i in dish:
        print(i)
        var = dic[i]
        for v in var:
            cook[v['ingredient_name']] = {'quantity': int(v['quantity']) * persons, 'measure': v['measure']}
    
    pprint(cook)       

get_shoy_dishes(cook_book, ['Запеченный картофель', 'Омлет'], 7)






    
