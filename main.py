from character import Character
from inventory import Inventory
from items import Item

# Tracks user input as choice
choice = "a"

# Can use this anytime player input is required to include global commands
def Global_choice(res=input()):
    if res == "P":
        player.Consume_potion()
        print("You consumed 1 potion restoring 20 health. Your health is now", player.hp, "and you have", player.inv_potion, "potions.")
    if res == "CS":
        player.Check_stats()
    else:
        global choice 
        choice = res
    
player = Character(name=input("Choose a name for your character: "), attack=20, hp=200, defense=1, inv_potion=10)

        
backpack = Inventory('Backpack', 10, 'back')
fannypack = Inventory('Fannypack', 5, 'waist')
backpack.equip(player)
fannypack.equip(player)
marijuana_b = Item(name="Marijuana", description="Marijauna is a plant that has psychoactive properties when consumed. Make sure to bring this to the Ganja Beige Knight show!", individual_value=15)
marijuana_f = Item(name="Marijuana", description="Marijauna is a plant that has psychoactive properties when consumed. Make sure to bring this to the Ganja Beige Knight show!", individual_value=15)
player.show_equipped()