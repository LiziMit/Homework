
with open ("recipes.txt", "r", encoding="utf-8") as file:
    dic = {}
    for line in file:
        dish = line.strip()
        print(dish)
        dic[dish] = []
        ingredients = int(file.readline().strip())
        print(ingredients)
        for i in range(ingredients):
            str = file.readline().strip()
            str_sp = str.split(" | ")
            print(str_sp)
            dic[dish] = [{'ingredient_name': str_sp[0], 'quantity': str_sp[1], 'measure': str_sp[2]}]
        file.readline()
        print()
    print(dic)
    



    
