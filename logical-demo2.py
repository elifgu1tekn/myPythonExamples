# Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesapla 
# Formül: (kilo/(boy*2))
# Aşağıdaki tabloya göre kişi hangi gruba girer?
# 0-18.4 => Zayıf
# 18.5-24.9 => Normal
# 25.0-29.9 => Fazla Kilolu
# 30.0-34.9 => Şişman (obez)

name = input("Kullanici adi: ")
kg = float(input("Kilosu: "))
hg = float(input("Boyu: "))

indeks = (kg / (hg * 2))

result = (indeks >= 0) and (indeks <=18.4)
print(f"Zayif mi: {result}")

result = (indeks >= 18.5) and (indeks <=24.9)
print(f"Normal mi: {result}")

result = (indeks >= 25.0) and (indeks <=29.9)
print(f"Fazla Kilolu mu: {result}")

result = (indeks >= 30.0) and (indeks <=34.9)
print(f"Obez mi: {result}")

