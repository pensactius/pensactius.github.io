craft_items = {
    "Axe": {
        "Twigs": 1,
        "Flint": 1,    
    },
    "PicAxe": {
        "Twigs": 2,
        "Flint": 2
    }
}

def remove_from_inventory(inventory, ingredients):
    for item in ingredients:
        print(f'\x1b[37;2mRemoving {ingredients[item]} {item}\x1b[0m')
        del inventory[item]

def add_to_inventory(inventory, item):
    if item in inventory:
        inventory[item] += 1
    else:
        inventory[item] = 1

# {'Twigs': 1, 'Flint': 1}
def has_required_ingredients(inventory, ingredients):
    has_all_ingredients = True

    for item in ingredients:
        ammount_required = ingredients[item]
        if item in inventory:
            ammount_in_inventory = inventory[item]
        if not item in inventory or ammount_required > ammount_in_inventory:
            has_all_ingredients = False
    return has_all_ingredients
    
def craft(item, inventory):
    ingredients = craft_items[item]
    print(f'\x1b[37;1mCrafting 1 {item}\x1b[36;0;3m. Needs {ingredients}\x1b[0m')
    
    if has_required_ingredients(inventory, ingredients):        
        remove_from_inventory(inventory, ingredients)
        add_to_inventory(inventory, item)
    else:
        print('\x1b[31;1mNot enough ingredients to craft', item, '\x1b[0m')

def print_inventory(inventory):
    print('\x1b[36;1mInventory: \x1b[37;1m', inventory, '\x1b[0m')

def pick_up(inventory, item):
    add_to_inventory(inventory, item)
    print('Picking up 1 \x1b[35;1m', item, '\x1b[0m')
    

def run():
    inventory = {}

    print_inventory(inventory)
    craft('Axe', inventory)
    
    for item in ['Twigs', 'Flint']:
        pick_up(inventory, item)
    print_inventory(inventory)
    
    craft('Axe', inventory)
    print_inventory(inventory)
    
    for item in ['Twigs', 'Twigs']:       
        pick_up(inventory, item)
    print_inventory(inventory)
        
    craft('PicAxe', inventory)
    print_inventory(inventory)
    
    for item in ['Flint', 'Flint']:
        pick_up(inventory, item)
        
    craft('PicAxe', inventory)
    print_inventory(inventory)

if __name__ == '__main__':
    run()