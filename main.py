class Character():
    name = ""
    starting_health = 1.0
    health = 1.0
    attack = 1.0
    defense = 1.0
    inv_potion = 0
    # is_alive is True by default. set is_alive=False in Character kwargs if you want a dead character
    is_alive = True
    
    def __init__(self, **kwargs):
        self.name = kwargs["name"] if "name" in kwargs else "LOSER"
        self.health = kwargs["health"] if "health" in kwargs else 100
        self.starting_health = kwargs["health"] if "health" in kwargs else 100
        self.attack = kwargs["attack"] if "attack" in kwargs else 1
        self.defense = kwargs["defense"] if "defense" in kwargs else 0
        self.inv_potion = kwargs["inv_potion"] if "inv_potion" in kwargs else 0
        self.is_alive = kwargs["is_alive"] if "is_alive" in kwargs else True
    
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
        self.health -= truedamage
        if self.health <= 0:
            self.Die()
            
    def Die(self):
        self.is_alive = False
        self.health = 0
        
    def Revive(self):
        self.is_alive = True
        self.health = (self.starting_health / 2)
        
player = Character(name=input("Choose a name for your character: "), health=100, attack=2, defense=5, inv_potion=10)
print(player.__dict__)
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
print(player.is_alive)