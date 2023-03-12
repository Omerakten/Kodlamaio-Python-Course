# Bir öğrenci kayıt sistemi yazdığımızı düşünelim.
# Sistemimizdeki öğrencileri bir listede sadece ad soyad olacak şekilde tutalım.

# Bu öğrenci kayıt sistemine;
# 1-Aldığı isim soy isim ile listeye öğrenci ekleyen
# 2-Aldığı isim soy isim ile eşleşen değeri listeden kaldıran
# 3-Listeye birden fazla öğrenci eklemeyi mümkün kılan
# 4-Listedeki tüm öğrencileri tek tek ekrana yazdıran
# 5-Öğrencinin listedeki index numarası öğrenci numarası olarak kabul edildiğini düşünerek
#   öğrencinin numarasını öğrenmeyi mümkün kılan
# 6 Listeden birden fazla öğrenci silmeyi mümkün kılan (döngü kullanınız)
# fonksiyonları geliştiriniz ve her bir fonksiyonu en az bir kere çağırarak konsolda test ediniz.
#
# Ödevde kullanacağınız döngülerin bir tanesi for bir tanesi while döngüsü olması istenmektedir.


print("-------------------------------------------------------------------")
print("----------------Öğrenci Kayıt Sistemine hoşgeldiniz----------------")
print("-------------------------------------------------------------------")
loop = True
students = ["ömer akten","cemre mısırlı","ercan erik"]

def menu():
    sec = input("Lütfen yapmak istediğiniz işlemi seçiniz: \n"
                "1 - Öğrenci Ekle\n"
                "2 - Öğrenci Sil\n"
                "3 - Öğrencileri Listele\n"
                "4 - Öğrenci Numarası Öğrenme\n"
                "5 - Sistemi Kapat ! ")
    if sec == "1":
        print("Kayıt ekleme menüsüne yönlendiriliyorsunuz.")
        print("-----------------------------------------------------------")
        addStudent()
    if sec == "2":
        print("Kayıt Silme menüsüne yönlendiriliyorsunuz.")
        print("-----------------------------------------------------------")
        removeStudent()
    if sec == "3":
        print("Öğrenciler listeleniyor...")
        print("-----------------------------------------------------------")
        studentsList()
    if sec == "4":
        print("Öğrenci Numarası öğrenme sayfasına gidiliyor...")
        print("-----------------------------------------------------------")
        studentNum()
    if sec == "5":
        print("Sistemden cıkış yapılıyor....")
        print("-----------------------------------------------------------")
        exıt()

def addStudent():
    print(students)
    add = input("Eklemek istediğiniz öğrencinin İsim ve soy ismini giriniz: \n ")
    students.append(add)
    print(students)
    def cont():
        print("-----------------------------------------------------------")
        sec = input("Daha fazla ekleme işlemi yapmak için --> 1\n"
                    "Devam etmek için -->2\n")
        if sec == "1":
            addStudent()
        if sec == "2":
            menuReturn()
        if sec not in ["1", "2"]:
            print("-----------------------------------------------------------")
            print("Lütfen geçerli bir seçenek giriniz.")
            cont()
    cont()

def removeStudent(): # COMPLETED
    print(students)
    remove = input("Silmek istediğiniz öğrencinin İsim ve soy ismini giriniz: \n ")
    if remove in students:
        students.remove(remove)
    else:
        print("-----------------------------------------------------------")
        print("hatalı giriş yaptınız veri bulunamadı tekrar deneyin")
        print("-----------------------------------------------------------")
        removeStudent()
    print(students)
    def cont():
        print("-----------------------------------------------------------")
        sec = input("Daha fazla ekleme işlemi yapmak için --> 1\n"
                    "Devam etmek için -->2\n")
        if sec == "1":
            removeStudent()
        if sec == "2":
            menuReturn()
        if sec not in ["1", "2"]:
            print("-----------------------------------------------------------")
            print("Lütfen geçerli bir seçenek giriniz.")
            cont()
    cont()

def studentsList():
    print(students)
    menuReturn()

def studentNum():
    print(students)
    num = input("Numrasını öğrenmek istediğiniz öğrencinin İsim ve soy ismini giriniz: \n ")
    stunum = students.index(num)
    print("{} Öğrencinin numarası: {} ".format(num,stunum))
    def cont():
        print("-----------------------------------------------------------")
        sec = input("Daha fazla ekleme işlemi yapmak için --> 1\n"
                    "Devam etmek için -->2\n")
        if sec == "1":
            studentNum()
        if sec == "2":
            menuReturn()
        if sec not in ["1", "2"]:
            print("-----------------------------------------------------------")
            print("Lütfen geçerli bir seçenek giriniz.")
            cont()
    cont()

def menuReturn():
    print("-----------------------------------------------------------")
    sec = input("Lütfen yapmak istediğiniz işlemi seçiniz:\n"
                "1 - Ana menüye dön\n"
                "2 - Sistemi Kapat")
    if sec == "1":
        print("-----------------------------------------------------------")
        print("Ana menüye yönlendiriliyorsunuz.")
        menu()
    if sec == "2":
        print("-----------------------------------------------------------")
        print("Sistem kapanıyor....")
        exıt()
    if sec not in ["1", "2"]:
        print("-----------------------------------------------------------")
        print("Lütfen geçerli bir seçenek giriniz.")
        menuReturn()

def exıt():
    print("-----------------------------------------------------------")
    print("sistemden cıkış yapılıyor.....")
    loop = False
    exit()

while loop:
    menu()