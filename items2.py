class Items:
    def __init__(self, choice):
        items = ['rock', 'paper', 'scizzors']
        
        if choice not in items:
            raise ValueError(f'{choice}: Invalid choice')
        
        self.choice = choice
        
        
master_marijauana_list = [marijuana_1, marijauna_2]
used_marijuana_list = [marijuana_1]
        
def getitem():
    for i in master_marijauana_list:
        if i not in used_marijuana_list:
            return i
        
inventory.items.append(getitem())

inventory.items.append(marijuana_2)
            