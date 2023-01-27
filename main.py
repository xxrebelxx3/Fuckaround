from character import Character

player = Character(name=input("Choose a name for your character: "), attack=20, health=200, defense=1, inv_potion=10)
enemy1 = Character(name="Killa", attack=5, defense=5)

print(player.__dict__)
print(enemy1.__dict__)

player.Dmg(100)
player.Check_stats()
choice = input("Press P to drink a potion")

if choice == "P":
    player.Consume_potion()
player.Check_stats()
