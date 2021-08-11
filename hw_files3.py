from os import read
from pprint import pprint
my_list = ['1.txt','2.txt','3.txt']
list = []
my_dict = {}
for name in my_list:
    with open (name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        my_dict[name] = len(lines)
        list.append(my_dict)
        my_dict_sorted = sorted(my_dict.items(), key=lambda x: x[1])
# print(my_dict_sorted)
for x, y in my_dict_sorted:    
    with open (x, 'r', encoding='utf-8') as file:
        print(x)
        print(y)
        print(file.read())
    
 