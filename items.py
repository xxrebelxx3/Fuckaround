class Item:

    def __init__(self, name, description, individual_value):
        self.name = name
        self.description = description
        self.amount = 0
        self.individual_value = individual_value

    @property
    def worth(self):
        return f'${self.amount * self.individual_value:.2f}'

    def sell(self, inventory):
        if self in inventory.items:
            if self.amount >= 0.1:
                print('How many do you want to sell?')
                amt = float(input('amt > '))
                if amt > self.amount:
                    print(f"You only have {self.amount} of {self.name}.")
                else:
                    print(f'Are you sure you want to sell {amt} {self.name} for ${self.individual_value * amt:.2f}?')
                    confirm = input('[y/n] > ')
                    if confirm == 'y':
                        self.amount -= amt
                        print(f'{amt} {self.name} sold for ${amt * self.individual_value:.2f}!')
                    else:
                        pass

            pass
        else:
            print(f"You are not currently carrying any {self.name}.")

    def add_to_inventory(self, inventory, amount):
        if len(inventory.items) < inventory.capacity:
            if self not in inventory.items:
                self.amount = amount
                inventory.items.append(self)
                print(f'x{self.amount} {self.name} added to your Inventory')
            else:
                self.amount += amount
                print(f'x{amount} {self.name} added to your Inventory. You now have x{self.amount} {self.name}')

        else:
            print('No room for more items...')