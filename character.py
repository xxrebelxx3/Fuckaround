class Character():
    
    # default character creation values unless specified in character creation
    def __init__(self, name="John Doe", age=18, hp=100, char_type="Noob", subclass="None", has_weapon=False, has_armor=False, attack=1, defense=0, inv_potion=0, reputation=50, is_alive=True):
        self.name = name
        self.age = age
        self.hp = hp
        # Wook, spiritual, old head, Prepared for everything.
        self.char_type = char_type
        # Shaman, Healer, Dealer, artist, slut etc. Can be multiple
        self.subclass = subclass
        self.starting_hp = hp
        # attacks is base damage a character deals
        self.attack = attack
        self.starting_attack = attack
        # defense reduces damage dealt to character by value of defense. See Dmg.
        self.defense = defense
        self.starting_def = defense
        self.inv_potion = inv_potion
        self.is_alive = is_alive
        self.has_weapon = has_weapon
        self.has_armor = has_armor
        # 50 is neutral, 0 is worst, 100 is best.
        self.reputation = reputation
        
    # prints character values
    def Check_stats(self):
        print("Name =", self.name)
        print("Age =", self.age)
        print("Character Type =", self.char_type)
        print("SubClass =", self.subclass)
        print("hp =", self.hp)
        print("Attack =", self.attack)
        print("Defense =", self.defense)
        print("Potion Inventory =", self.inv_potion)
        print("Armor Equipped =", self.has_armor)
        print("Weapon Equipped =", self.has_weapon)
        print("Is Alive =", self.is_alive)
        print("Reputation =", self.reputation)
    # adds potion to character inventory
    def Add_potion(self, value):
        self.inv_potion += value
        
    # drinks potion: adds 20 health, subtracts 1 potion from inventory
    def Consume_potion(self):
        if self.inv_potion > 0:
            self.Heal(20)
            self.inv_potion -= 1
        else:
            print("You do not have any potions")
            
    # adds specified health to character
    def Heal(self, value):
        if self.is_alive:
            self.hp += value
            if self.hp > self.starting_hp:
                self.hp = self.starting_hp
        else:
            print("Nice try, but you are already dead")
            
    # equips a weapon: adds specified value to characters attack
    def Equip_wep(self, value):
        if self.has_weapon == False:
            self.attack += value
            self.has_weapon = True
        else:
            print("You already have a weapon equiped")
            
    # unequips weapon: resets character attack to starting attack
    def Unequip_wep(self):
        if self.has_weapon:
            self.has_weapon = False
            self.attack = self.starting_attack
        else:
            print("You do not have a weapon equipped")
            
    # equips armor: adds specified value to characters defense
    def Equip_armor(self, value):
        if self.has_armor == False:
            self.defense += value
            self.has_armor = True
        else:
            print("You are already wearing armor")
            
    # unequip armor: resets character defense to starting defense
    def Unequip_armor(self):
        if self.has_armor:
            self.defense = self.starting_def
            self.has_armor = False
        else:
            print("You are not wearing any armor")
                
    # calculates and applies damage as value-character defense. can use self.attack as value     
    def Dmg(self, value):
        truedamage = value - self.defense
        if truedamage < 0:
            truedamage = 0
        self.hp -= truedamage
        if self.hp <= 0:
            self.Die()
            
    # kills character: sets health to 0 and is_alive to False
    def Die(self):
        self.is_alive = False
        self.hp = 0
        
    # revives character: sets health to half starting health and sets is_alive to True
    def Revive(self):
        self.is_alive = True
        self.hp = (self.starting_hp / 2)
   
# examples of character creation:     
# player = Character(name=input("Choose a name for your character: "), attack=20, hp=200, defense=1, inv_potion=10)
# enemy1 = Character(name="Killa", attack=5, defense=5)
