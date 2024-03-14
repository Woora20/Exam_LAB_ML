class Menu:
    def __init__(self):
        self.name = ""
        self.dishes = [{'name': '', 'description': '', 'price': 0}]

    def show(self):
        print(self.name)
        for index, dish in enumerate(self.dishes, start=1):
            print('{:d}. {:s}. {:s}. {:.2f}'.format(
                index, dish['name'], dish['description'], dish['price']))

    def new_dish(self, dish_dict):
        self.dishes.append(dish_dict)

    def remove_dish(self, dish_number):
        if 1 <= dish_number <= len(self.dishes):
            del self.dishes[dish_number - 1]

    def update_price(self, dish_number, new_price):
        if 1 <= dish_number <= len(self.dishes):
            self.dishes[dish_number - 1]['price'] = new_price

if __name__ == '__main__':
    m1 = Menu()
    m1.name = "Tasty and Healthy"
    m1.dishes = [
        {'name': 'Kang Saparot', 'description': 'Mussel pineapple curry', 'price': 120},
        {'name': 'Jeolhon', 'description': 'Basil spicy hotpot', 'price': 200}
    ]
    
    m1.show()
    
    print('\nNew dish')
    m1.new_dish({'name': 'Sup Kanoon', 'description': 'Smashed jackfruit salad', 'price': 50})
    m1.show()
    
    print('\nRemove dish')
    m1.remove_dish(2)
    m1.show()
    
    print('\nUpdate')
    m1.update_price(1, 110)
    m1.show()


# Output
# Tasty and Healthy
# 1. Kang Saparot. Mussel pineapple curry. 120.00
# 2. Jeolhon. Basil spicy hotpot. 200.00

# New dish
# Tasty and Healthy
# 1. Kang Saparot. Mussel pineapple curry. 120.00
# 2. Jeolhon. Basil spicy hotpot. 200.00
# 3. Sup Kanoon. Smashed jackfruit salad. 50.00

# Remove dish
# Tasty and Healthy
# 1. Kang Saparot. Mussel pineapple curry. 120.00
# 2. Sup Kanoon. Smashed jackfruit salad. 50.00

# Update
# Tasty and Healthy
# 1. Kang Saparot. Mussel pineapple curry. 110.00
# 2. Sup Kanoon. Smashed jackfruit salad. 50.00