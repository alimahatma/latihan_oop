class Hero:
    #class variabel
    jumlah_hero = 0

    def __init__(self, inputNama, inputHealth, inputPower, inputArmor):
        #instance variabel
        self.name = inputNama
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor

        #akses variabel class untuk menghitung jumlah hero
        Hero.jumlah_hero += 1
        
    #1. Metohd tipe pertama, Membuat method tanpa return (void function)
    def siapa(self):
        print("Namaku adalah : " + self.name)
    
    #2. Method tipe keduamembuat method dengan argumen
    def healthUp(self, up):
        self.health += up

    #3. Method tipe ketiga method dengan return
    def getHealth(self):
        return self.health

hero1 = Hero('sniper', 100, 10, 5)
hero2 = Hero('mario bros', 90, 5, 10)

#menampilkan atribut pada objek hiro
print(hero1.__dict__)
print(hero2.__dict__)

#menampilkan atribut pada objek hiro1 pada objek dengan method
hero1.siapa()

#menampilkan aksi health up pada hiro1
hero1.healthUp(10)
print("hasil method dengan argumen tanpa return", hero1.health)

#menampilkan aksi pada method ketiga
print("hasil method dengan argumen tanpa return", hero1.getHealth()) 
print("jumlah hiro sebanyak ", Hero.jumlah_hero)