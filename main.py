from character import Character

choice = "a"

def Global_choice(res=input()):
    if res == "P":
        player.Consume_potion()
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

res = input("Enter \"P\" to consume a potion or \"CS\" to check player statistics: ")
if res == "P":
    player.Consume_potion()
if res == "CS":
    player.Check_stats()

Global_choice(input("Enter \"P\" to consume a potion or \"CS\" to check player statistics: "))
if choice == "L":
    print("You go left")