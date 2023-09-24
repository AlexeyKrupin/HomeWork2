def read_file(name_file):
    cook_book = {}
    with open(name_file, 'r', encoding='cp1251') as file:
        name_dishes = ''
        for line in file:
            clean_line = line.strip()
            if not clean_line:
                continue
            if not name_dishes:
                name_dishes = clean_line
                continue
            if clean_line.isdigit():
                ingr_count = int(clean_line)
                ingr_list = []
                for i in range(ingr_count):
                    ingr_info = file.readline().strip().split('|')
                    if len(ingr_info) == 3:
                        ingr = {'ingredient_name': ingr_info[0], 'quantity': int(ingr_info[1]), 'measure': ingr_info[2]}
                        ingr_list.append(ingr)
                cook_book[name_dishes] = ingr_list
                name_dishes = ''
    return cook_book


cook_book = read_file('cook_book.txt')


# for i in cook_book.items():
#     print(i)

def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingr in cook_book[dish]:
                ingredient_name = ingr['ingredient_name']
                quantity = ingr['quantity'] * person_count
                measure = ingr['measure']
                if ingredient_name in shop_list:
                    shop_list[ingredient_name]['quantity'] += quantity
                else:
                    shop_list[ingredient_name] = {'quantity': quantity, 'measure': measure}
    return shop_list



dishes_to_cook = ['Борщ', 'Паста с креветками']
person_count = 2
shopping_list = get_shop_list_by_dishes(dishes_to_cook, person_count, cook_book)
print(shopping_list)