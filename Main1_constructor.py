class Hero: #template

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        #instance variabel
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor

hero1 = Hero("Sniper", 100, 10, 4)
hero2 = Hero("Mirana", 100, 14, 1)
hero3 = Hero("Ucup", 1000,10, 0)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)
