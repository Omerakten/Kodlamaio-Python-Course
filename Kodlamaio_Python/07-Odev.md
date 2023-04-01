# PyTestdeki decoratorleri araştırarak oluşturduğunuz notları bir "ReadMe" dosyası olarak githubda paylaşınız.

Decoratorlar var olan fonksiyonlarımıza özellikler eklemeye yararlar. Aslında decoraterlar da fonksiyondur. Fonksiyon isimlerinin başına @ işareti alarak decorater haline gelirler. 

```python
def decorator(fonk):
    def wrapper():
        print("Fonksiyon çalışmadan önceki işlemler")
        fonk()
        print("Fonksiyon çalıştıktan sonraki işlemler")
    return wrapper

@decorator
def fonksiyon():
    print("fonksiyon çalışıyor")

# Alltaki iki satır yerine fonksiyon() methodunun üstüne @decorator yazarsak aynı işlemi yapmış oluruz 
# fonksiyon2=decorator(fonksiyon)
# fonksiyon2()
fonksiyon()
```

Başka bir örnek: 
```python
def ikiyle_carp(func):
    def wrapper(x,y):
        func(x*2,y*2)
    return wrapper

@ikiyle_carp
def topla(x,y):
    print(x+y)

topla(5,10)
```

# Pytest Decoratorleri
@pytest.mark.skip: Testi atlar, test çalıştırılmaz.

@pytest.mark.skipif: Belirli bir koşula bağlı olan testi atlar.

@pytest.mark.parametrize: Birden fazla parametre vererek testi çalıştırmamızı sağlar.

@pytest.mark.xfail: Testin başarısız olmasını beklediğimizi belirtmek için kullanılır.

@pytest.mark.timeout: Testin belirli bir süre içinde tamamlanması gerektiğini belirtir.
