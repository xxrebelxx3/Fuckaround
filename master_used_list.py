from items import Item


marijuana_template = Item(name="Marijuana", description="Marijauna is a plant that has psychoactive properties when consumed. Make sure to bring this to the Ganja Beige Knight show!", individual_value=15)

def clone(item):
    return Item(item.name, item.description, item.individual_value)


used_dict = []
master_dict = {}

for i in range(1, 20):
    key = "m" + str(i)
    master_dict[key] = clone(marijuana_template)

print(master_dict)

def getitem(masterlist, usedlist):
    for i in masterlist:
        if i not in usedlist:
            usedlist.append(i)
            return i
        
master_dict = {}

for i in range(1, 20):
    key = "m" + str(i)
    master_dict[key] = clone(marijuana_template)

print(master_dict)
