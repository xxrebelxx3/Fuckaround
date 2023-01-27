from character import Character

def Global_choice(res):
    if res == "P":
        player.Consume_potion
    if res == "CS":
        player.Check_stats
        
player = Character(name=input("Choose a name for your character: "), attack=20, hp=200, defense=1, inv_potion=10)
enemy1 = Character(name="Killa", attack=5, defense=5)

print(player.__dict__)
print(enemy1.__dict__)

player.Dmg(100)
player.Check_stats()
res = input("Enter \"P\" or \"POTION\" to drink a potion: ")
print(res)
Global_choice("P")
res = input("Enter \"CS\" or \"CHECKSTATS\" to check player statistics: ")
print(res)
Global_choice("CS")
