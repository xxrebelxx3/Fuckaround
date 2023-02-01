from character import Character
from inventory import Inventory
from items import Item

player = Character(name=input("Choose a name for your character: "), attack=20, hp=200, defense=1, inv_potion=10)
backpack = Inventory('Backpack', 10, 'back')
fannypack = Inventory('Fannypack', 5, 'waist')
marijuana_1 = Item(name="Marijuana", description="Marijauna is a plant that has psychoactive properties when consumed. Make sure to bring this to the Ganja Beige Knight show!", individual_value=15)
marijuana_2 = Item(name="Marijuana", description="Marijauna is a plant that has psychoactive properties when consumed. Make sure to bring this to the Ganja Beige Knight show!", individual_value=15)
marijuana_3 = Item(name="Marijuana", description="Marijauna is a plant that has psychoactive properties when consumed. Make sure to bring this to the Ganja Beige Knight show!", individual_value=15)


master_marijauana_list = [marijuana_1, marijuana_2, marijuana_3, marijuana_4, marijuana_5]
used_marijuana_list = [marijuana_1]
# Tracks user input as choice
choice = "a"

# Can use this anytime player input is required to include global commands
def Global_choice():
    res = input()
    if res == "P":
        player.Consume_potion()
        print("You consumed 1 potion restoring 20 health. Your health is now", player.hp, "and you have", player.inv_potion, "potions.")
    if res == "CS":
        player.Check_stats()
    else:
        global choice 
        choice = res
        


def getitem():
    for i in master_marijauana_list:
        if i not in used_marijuana_list:
            used_marijuana_list.append(i)
            return i

print(getitem())
print(getitem())
print(getitem())


    

        

# player.equip_inventory(backpack)
# player.equip_inventory(fannypack)
# backpack.show_inventory()
# marijuana_b = Item(name="Marijuana", description="Marijauna is a plant that has psychoactive properties when consumed. Make sure to bring this to the Ganja Beige Knight show!", individual_value=15)
# marijuana_f = Item(name="Marijuana", description="Marijauna is a plant that has psychoactive properties when consumed. Make sure to bring this to the Ganja Beige Knight show!", individual_value=15)
# test_item = Item(name="test", description="This is a test item", individual_value=100)
# player.show_equipped()
# test_item.add_to_inventory(backpack, 50)
# marijuana_b.add_to_inventory(backpack, 10)
# marijuana_f.add_to_inventory(fannypack, 10)
# backpack.show_inventory()
# backpack.transfer(fannypack)
# fannypack.transfer(backpack)
# backpack.transfer(fannypack)
