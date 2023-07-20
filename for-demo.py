sayilar = [1,3,5,7,9,12,19,21]

# Listedeki hangi sayılar 3'ün katı
for s in sayilar:
    if(s % 3 == 0):
        print(s)

# Listedeki sayilarin toplamı
toplam = 0
for s in sayilar:
    toplam += s

print(f'toplam: {toplam}')

# Listedeki tek sayıların karesi
for s in sayilar:
    if(s % 2 == 1):
        print((s ** 2))


sehirler = ['kocaeli', 'istanbul', 'ankara', 'izmir', 'rize']

# Şehirlerden hangileri en fazla 5 karakterli?
for sehir in sehirler:
    if (len(sehir)<=5):
        print(sehir)

urunler = [
    { 'name': 'samsung S6', 'price': '3000' },
    { 'name': 'samsung S7', 'price': '4000' },
    { 'name': 'samsung S8', 'price': '5000' },
    { 'name': 'samsung S9', 'price': '6000' },
    { 'name': 'samsung S10', 'price': '7000' },
]

# Ürünlerin fiyatlar toplamı
toplam = 0
for urun in urunler:
    fiyat = int(urun['price'])
    toplam += fiyat
print(f'Toplam: {toplam}')

# Fiyatı en fazla 5000 olan ürünleri göster
for urun in urunler:
    if( (int(urun['price'])) <= 5000):
        print(urun['name'])
