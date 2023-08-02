# Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yaz
def yazdir(kelime, adet):
    print(kelime * adet)

yazdir("Merhaba\n", 5)

# Kendine gönderilen sınırsız sayıdaki paramtreyi bir listeye çeviren fonksiyon
def listCevir(*params):
    list = []

    for param in params:
        list.append(param)

    return list

result = listCevir(1, 2, 3, 'Selam')
print(result)

# Gönderilen iki sayı arasındaki tüm asal sayıları bul
s1 = int(input("1. sayi: "))
s2 = int(input("2. sayi: "))

def asalBul(s1, s2):
    for sayi in range(s1, s2+1):
        if sayi > 1:
            for i in range(2, sayi):
                if (sayi % i == 0):
                    break
            else:
                print(sayi)

asalBul(s1, s2)

# Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndür
def tamBolen(sayi):
    tamBolenler = []

    for i in range(2, sayi):
        if(sayi % i == 0):
            tamBolenler.append(i)
    
    return tamBolenler

print(tamBolen(36))
