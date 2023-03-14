#PYTHON CLASS
class Banka:
    def krediBasvur(self):
        print("kredi başvurusu yapıldı")
    def krediHesapla(self):
        print("hesaplar yapıldı")

banka = Banka()
banka.krediBasvur()

#self = this

####################################################################################

class Matematik:
    def __init__(self,sayi1,sayi2): #constructor yapıcı
        print("Matematik başladı (referansı oluştu)")
        self.sayi1= sayi1
        self.sayi2= sayi2

    def topla(self):
         return self.sayi1 + self.sayi2
    def cikar(self):
         return self.sayi1 - self.sayi2
    def bol(self):
         return self.sayi1 / self.sayi2
    def carp(self):
         return self.sayi1 * self.sayi2

matematik = Matematik(8,7)
sonuc = matematik.topla()
print("sonuc: "+str(sonuc))

####################################################################################

class Istatistik(Matematik): #İnheritance
    def __init__(self,sayi1,sayi2):
        super().__init__(sayi1,sayi2)

    def varyansHesapla(self):
        return self.sayi1 * self.sayi2


istatistik = Istatistik(5,8)
sonuc = istatistik.carp()
print("sonuc: "+str(sonuc))

####################################################################################


class Person:
    def __init__(self,name,lastname):
        self.name = name
        self.lastname = lastname



musteri1 = Person("Ahmet","Demiroğ")
musteri2 = Person("Kerem","Varış")
musteri3 = Person("İlker","Tural")

print(musteri1.name)

####################################################################################


