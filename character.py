class Character():
    
    def __init__(self, name, hp=100, has_weapon=False, has_armor=False, attack=1, defense=0, inv_potion=0, is_alive=True):
        self.name = name
        self.hp = hp
        self.starting_hp = hp
        self.attack = attack
        self.starting_attack = attack
        self.defense = defense
        self.starting_def = defense
        self.inv_potion = inv_potion
        self.is_alive = is_alive
        self.has_weapon = has_weapon
        self.has_armor = has_armor
    
    def Check_stats(self):
        print("Name =", self.name)
        print("hp =", self.hp)
        print("Attack =", self.attack)
        print("Defense =", self.defense)
        print("Potion Inventory =", self.inv_potion)
        print("Armor Equipped =", self.has_armor)
        print("Weapon Equipped =", self.has_weapon)
        print("Is Alive =", self.is_alive)
        
    def Add_potion(self, value):
        self.inv_potion += value
        
    def Consume_potion(self):
        if self.inv_potion > 0:
            self.Heal(20)
            self.inv_potion -= 1
        else:
            print("You do not have any potions")
            
    def Heal(self, value):
        if self.is_alive:
            self.hp += value
            if self.hp > self.starting_hp:
                self.hp = self.starting_hp
        else:
            print("Nice try, but you are already dead")
            
    def Equip_wep(self, value):
        if self.has_weapon == False:
            self.attack += value
            self.has_weapon = True
        else:
            print("You already have a weapon equiped")
            
    def Unequip_wep(self):
        if self.has_weapon:
            self.has_weapon = False
            self.attack = self.starting_attack
        else:
            print("You do not have a weapon equipped")
            
    def Equip_armor(self, value):
        if self.has_armor == False:
            self.defense += value
            self.has_armor = True
        else:
            print("You are already wearing armor")
            
    def Unequip_armor(self):
        if self.has_armor:
            self.defense = self.starting_def
            self.has_armor = False
        else:
            print("You are not wearing any armor")
                        
    def Dmg(self, value):
        truedamage = value - self.defense
        if truedamage < 0:
            truedamage = 0
        self.hp -= truedamage
        if self.hp <= 0:
            self.Die()
            
    def Die(self):
        self.is_alive = False
        self.hp = 0
        
    def Revive(self):
        self.is_alive = True
        self.hp = (self.starting_hp / 2)
        
# player = Character(name=input("Choose a name for your character: "), attack=20, hp=200, defense=1, inv_potion=10)

# enemy1 = Character(name="Killa", attack=5, defense=5)
# print(player.__dict__)
# print(enemy1.__dict__)

"""while player.is_alive and enemy1.is_alive:
    print("you have been attacked")
    player.Dmg(enemy1.attack)
    print("you have taken", (enemy1.attack - player.defense), "damage leaving you with", player.hp)"""