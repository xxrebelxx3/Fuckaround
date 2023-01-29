
class Inventory():
    # example: backpack = Inventory(10)
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

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


# inspired by https://github.com/ngeorgj/rpg-inventory-system/blob/master/inventory.py