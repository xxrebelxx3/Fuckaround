
class Inventory():
    # example: backpack = Inventory(10, back)
    def __init__(self, name, capacity, location):
        self.name = name
        self.capacity = capacity
        self.items = []
        self.location = location

    """def equip_inventory(self, character, location_check=False):
        if len(character.wearing) < character.wear_capacity:
            if self not in character.wearing:
                for slot in character.wearing:
                    if slot.location == self.location:
                        location_check = True
                if location_check == True:
                    print(f"You are already wearing someting on your {character.location}")
                else:
                    character.wearing.append(self)
                    print(f'You have equipped {self.name} to {character.name}')
            else:
                print(f"You are already wearing a {self.name}")
        else:
            print("You are already wearing as much as you can carry")"""   
           
    def show_inventory(self):
        if len(self.items) > 0:
            print(f'Your {self.name} conatins:')
            index = 1
            for item in self.items:
                print(str(f'{index} -> [x{item.amount}] {item.name}'))
                index += 1
        else:
            print(f"Your {self.name} is empty.")

    def drop_item(self):
        print('\nWhich item do you want to drop? ["0" to Quit]')
        self.show_inventory()
        i = int(input('\nNº > '))
        if i == 0:
            print('\nClosing the Inventory...')
            return

        item = self.items[i - 1]
        if item.amount == 0.1:
            amt = 0.1
            self.items.pop(i - 1)
            print(f'Item {item.name}[x{amt}] Dropped!\nNow your Inventory is this:')

        else:
            print(f'You have {item.amount} of this, how many do you want to drop?')
            amt = float(input('amt > '))
            item.amount -= amt
            if item.amount <= 0:
                self.items.pop(i - 1)
                print(f'Item {item.name}[x{amt}] Dropped!\nNow your Inventory is this:')
            else:
                print(f'Item {item.name}[x{amt}] Dropped!\nNow your Inventory is this:')

        self.show_inventory()
        self.drop_item()
        
    def transfer(self, inventory2):
        print(f'\nWhich item do you want to transfer to your {inventory2.name}? ["0" to Quit]')
        self.show_inventory()
        i = int(input('\nNº > '))
        if i == 0:
            print('\nClosing the Inventory...')
            return

        item = self.items[i - 1]
        if item.amount == 0.1:
            amt = 0.1
            self.items.pop(i - 1)
            item.add_to_inventory(inventory2, amt)
            print(f'Item {item.name}[x{amt}] transfered from {self.name} to {inventory2.name}!\nNow your inventory is this:')

        else:
            print(f'You have {item.amount} of this, how many do you want to transfer?')
            amt = float(input('amt > '))
            if amt > item.amount:
                amt = item.amount
            item.amount -= amt
            item.add_to_inventory(inventory2, amt)
            if item.amount <= 0:
                self.items.pop(i - 1)
                print(f'Item {item.name}[x{amt}] transfered from {self.name} to {inventory2.name}!\nNow your {self.name} inventory is this:')
            else:
                print(f'Item {item.name}[x{amt}] transfered from {self.name} to {inventory2.name}!\nNow your {self.name} inventory is this:')

        self.show_inventory()
        print(f"And your {inventory2.name} contains:")
        inventory2.show_inventory()
        self.transfer(inventory2)

    @property
    def total_worth(self):
        return f'\nThe inventory Total Worth is: ${sum([i.individual_value * i.amount for i in self.items]):.2f}'

"""
Inventory templates:
    backpack = Inventory("Backpack", 10, 'back')
    fannypack = Inventory("Fannypack", 5, 'waist')
"""



# inspired by https://github.com/ngeorgj/rpg-inventory-system/blob/master/inventory.py