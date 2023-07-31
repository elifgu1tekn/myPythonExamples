sayilar = [1,3,5,7,9,12,19,21]

# sayilar listesini while ile ekrana yazdır
i = 0
while (i < len(sayilar)):
    print(sayilar[i])
    i += 1

# Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tek sayıları ekrana yazdır
bas =int(input("Başlangıç değerini gir: "))
bit = int(input("Bitiş değerini gir: "))

i = bas
while (bit > i):
    i += 1
    if (i % 2 == 1):
        print(i)
if (bit <= bas):
    print("Girilen değer geçersiz!!!")      

# 1-100 arasındaki sayıları azalan şekilde yazdır
i = 100
while i > 0:
    print(i)
    i -= 1

# Kullanıcıdan alınan 5 sayıyı ekrana sıralı yazdır
sayilar = []
i = 0
while i < 5:
    sayi = int(input("sayı: "))
    sayilar.append(sayi)
    i += 1
sayilar.sort()
print(sayilar)

# Kullanıcıdan alınan sınırsız ürün bilgisini urunler listesi içinde sakla 
# ** ürün sayısını kullanıcıya sor
# ** dictionary liste yapısı (name, price) şeklinde olsun
# ** ürün ekleme bittiğinde ürünleri ekrana while ile listele
urunler = []
adet = int(input("Ürün adedi: "))
i = 0
while (i < adet):
    name = input("Ürün adı: ")
    price = input("Ürün fiyatı: ")
    urunler.append({
        'name': name,
        'price': price
    }) 
    i += 1
for urun in urunler:
    print(f'ürünün adı: {urun["name"]} ve ürünün fiyatı: {urun["price"]}')
