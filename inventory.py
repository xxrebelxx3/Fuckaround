
class Inventory():
    # example: backpack = Inventory(10, back)
    def __init__(self, name, capacity, location):
        self.name = name
        self.capacity = capacity
        self.items = []
        self.location = location

    def equip(self, character, location_check=False):
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
            print("You are already wearing as much as you can carry")    
           
    def show(self):
        index = 1
        for item in self.items:
            print(str(f'{index} -> [x{item.amount}] {item.name}'))
            index += 1

    def drop_item(self):
        print('\nWhich item do you want to drop? ["0" to Quit]')
        self.show()
        i = int(input('\nNº > '))
        if i == 0:
            print('\nClosing the Inventory...')
            quit()

        item = self.items[i - 1]
        if item.amount == 1:
            amt = 1
            self.items.pop(i - 1)
            print(f'Item {item.name}[x{amt}] Dropped!\nNow your Inventory is this:')

        else:
            print(f'You have {item.amount} of this, how many do you want to drop?')
            amt = float(input('amt > '))
            if item.amount <= 0:
                amt = 0
                self.items.pop(item)
                print(f'Item {item.name}[x{amt}] Dropped!\nNow your Inventory is this:')
            item.amount -= amt
            print(f'Item {item.name}[x{amt}] Dropped!\nNow your Inventory is this:')

        self.show()
        self.drop_item()
        
    """def transfer(self, inventory2, amount, exist=False):
        print('\nWhich item do you want to transfer? ["0" to Quit]')
        self.show()
        i = int(input('\nNº > '))
        if i == 0:
            print('\nClosing the Inventory...')
            quit()"""

    @property
    def total_worth(self):
        return f'\nThe inventory Total Worth is: ${sum([i.individual_value * i.amount for i in self.items]):.2f}'

"""
Inventory templates:
    backpack = Inventory("Backpack", 10, 'back')
    fannypack = Inventory("Fannypack", 5, 'waist')
"""



# inspired by https://github.com/ngeorgj/rpg-inventory-system/blob/master/inventory.py