def get_dict(file_name):
    cook_book = {}
    with open(file_name) as file:
        for line in file:
            dish = line.strip()
            cook_book[dish] = []
            ingredients_quantity = int(file.readline().strip())            
            for i in range(ingredients_quantity):
                ingredient_dict = {}
                ingredient = file.readline().strip().split(' | ')
                ingredient_dict['ingredient_name'] = ingredient[0]
                ingredient_dict['quantity'] = int(ingredient[1])
                ingredient_dict['measure'] = ingredient[2]
                cook_book[dish].append(ingredient_dict)
            file.readline()
    return cook_book
def main():
    result = get_dict('recipes.txt')
    print(result)
main()