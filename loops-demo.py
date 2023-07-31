# 1-100 arasında rastgele bir sayiyi aşağı yukarı ifadeleriyle kullanıcıya buldurmaya çalış.
# ** Hak bilgisini kullanıcıdan al ve puanı bu bilgiye göre hesapla
# ** 100 üzerinden puanlama yap.

import random

sayi = random.randint(1,10)
hak = int(input("Kaç hakkınız olsun?: "))
i = hak
sayac = 0

while  i > 0:
    i -= 1
    sayac += 1
    tahmin = int(input("Tahmin: "))

    if sayi == tahmin:
        print(f'Tebirkler Bildiniz!! Puanınız: {100 - (100/hak) * (sayac - 1)}')
        break
    elif sayi > tahmin:
        print("yukarı")
    else:
        print("aşağı")

    if i == 0:
        print(f"Hakkınız bitti.. Tutulan sayı: {sayi}")

