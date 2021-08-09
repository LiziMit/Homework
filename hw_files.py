
with open ("recipes.txt", "r", encoding="utf-8") as file:
    for line in file:
        dish = line.strip()
        print(dish)
        ingredients = int(file.readline().strip())
        for i in range(ingredients):
            print(file.readline().strip())
        file.readline()
        print()
    
    
    
    
    
# file = {}
#     for line1 in file:                           # Loop over all lines in the file
#         if line1.strip() == '':                # If the line is blank
#             continue                          # Skip the blank line
#         elif line1.startswith("group"):        # Else if line starts with group
#             file = line1.strip()                # Strip whitespace and save key
#             dic[file] = []                     # Initialize empty list
#         else:
#             dic[file].append(line1.split())     # Not key so append values

# print (file)