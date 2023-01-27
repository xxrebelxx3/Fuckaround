class Character():
    name = ""
    starting_health = 1.0
    health = 1.0
    attack = 1.0
    defense = 1.0
    inv_potion = 0
    # is_alive is True by default. set is_alive=False in Character kwargs if you want a dead character
    is_alive = True
    
    def __init__(self, name, health=100, attack=1, defense=0, inv_potion=0, is_alive=True):
        # can use kwargs or variable specifically.
        self.name = name
        self.health = health
        self.starting_health = health
        self.attack = attack
        self.defense = defense
        self.inv_potion = inv_potion
        self.is_alive = is_alive
    
    def Add_potion(self, value):
        self.inv_potion += value
        
    def Consume_potion(self):
        if self.inv_potion > 0:
            self.Heal(20)
            self.inv_potion -= 1
            
    def Heal(self, value):
        self.health += value
        if self.health > 100:
            self.health = 100
            
    def Dmg(self, value):
        truedamage = value - self.defense
        if truedamage < 0:
            truedamage = 0
        self.health -= truedamage
        if self.health <= 0:
            self.Die()
            
    def Die(self):
        self.is_alive = False
        self.health = 0
        
    def Revive(self):
        self.is_alive = True
        self.health = (self.starting_health / 2)
        
player = Character(name=input("Choose a name for your character: "), attack=20, defense=5, inv_potion=10)


print(player.__dict__)
"""player.Dmg(player.attack)
print(player.__dict__)
player.Add_potion(5)
print(player.inv_potion)
player.Heal(200)
print(player.__dict__)
player.Dmg(50)
print(player.__dict__)
player.Consume_potion()
print(player.__dict__)
player.Dmg(9001)
print(player.__dict__)
player.Revive()
print(player.__dict__)
player.Die()
print(player.is_alive) this is testing functions"""