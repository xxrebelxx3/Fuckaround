from character import Character

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
enemy1 = Character(name="Killa", attack=5, defense=5)

print(player.__dict__)
print(enemy1.__dict__)

player.Dmg(100)
player.Check_stats()

Global_choice(input("Enter \"P\" to consume a potion or \"CS\" to check player statistics anytime you are able to make a choice. Try it now: "))

while True:
    Global_choice(input("You come up to a fork in the road. Enter \"L\" to go left or \"R\" to go right: "))
    if choice == "L":
        print("You go left")
        break
    if choice == "R":
        print("You go right")
        break
    
while True:
    Global_choice(input("You find a found a magic well. Would you like to drink from it? \"Y/N\": "))
    if choice == "Y":
        player.Heal(45)
        print("You have healed for 45 health. Your health is now", player.hp)
        break
    if choice == "N":
        player.Dmg(10)
        print("A rock flies out of the mystical well and strikes you dealing", (10 - player.defense), "damage leaving you with", player.hp, "health")
        break