ingredients = {}
cook_book = {}


with open("recipes.txt", "r", encoding="utf-8") as file:
    for line in file:
        dishes_name = str(line.strip())
        quantity = int(file.readline().strip())
        cook_book[dishes_name] = []

        for i in range(quantity):
            ing = file.readline().strip().split("|")
            quantity_ing = int(ing[1])
            ingredients = {"ingredient_name": ing[0], "quantity": quantity_ing, "measure": ing[2]}
            cook_book[dishes_name].append(ingredients) 
            # print(ingredients)
        emp_str = file.readline().strip()
    print(cook_book)

print("================================>")


def get_shop_list_by_dishes(dishes, cook_book, person_count):
    more_ingredients = {}
   
    for dish in dishes:
        if dish in cook_book.keys():
            for value in cook_book[dish]:
                value['quantity'] *= person_count
                if value["ingredient_name"] in more_ingredients.keys():
                    value['quantity'] *= 2
                ing_name = value["ingredient_name"]
                more_ingredients[ing_name] = []
                more_ing = {"measure": value['measure'], "quantity": value['quantity']}
                more_ingredients[ing_name].append(more_ing)
    print(more_ingredients, "\n")


get_shop_list_by_dishes(['Фахитос', 'Омлет'], cook_book, 2)
