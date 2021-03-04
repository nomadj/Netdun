class Hero:
    race_attack = {"wizard": 30, "warrior": 50, "mage": 30}
    race_defense = {"wizard": 20, "warrior": 30, "mage": 40}
    race_magic = {"wizard": 50, "warrior": 20, "mage": 30}
    
    def __init__(self, race):
        self.health = 100
        self.hunger = 100
        self.race = race
        self.attack = self.race_attack[race]
        self.defense = self.race_defense[race]
        self.magic = self.race_magic[race]
        
        
