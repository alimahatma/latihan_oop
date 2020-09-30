class Hero: #template
    
    #class variabel
    jumlah = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        
        #instance variabel
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah += 1 #melakukan aksi penjumlahan kelipatan 1 setiap kali menambah instance
        print("membuat Hero dengan nama : " + inputName , inputPower)


hero1 = Hero("Sniper", 100, 10, 4) #memanggil instance variabel
print(Hero.jumlah) #memanggil class variabel
hero2 = Hero("Mirana", 100, 14, 1)
print(Hero.jumlah)
hero3 = Hero("Ucup", 1000,10, 0)
print(Hero.jumlah)


