# Girilen 2 sayıdan hangisi büyük?
s1= int(input("1. sayi: "))
s2 = int(input("2. sayi: "))

a = s1 > s2
print(f"1. sayi daha büyüktür: {a}")

# Kullanıcıdan 2 vize (%60) ve 1 final (%40) notu alıp ortalama hesapla. Eğer ort. 50 ve üstündeyse geçti.
vize1 = int(input("1. Vize notu: "))
vize2 = int(input("2. Vize notu: "))
final = int(input("Final notu: "))
ort = ((vize1 + vize2)/2)*0.6 + final*0.4
print(f" Not ortalaması: {ort} Başarı durumu: {ort>=50}")

# Girilen bir sayının çift mi olduğu
s = int(input("Bir sayi gir: "))
cift = s % 2 == 0 
print(cift)

# Girilen sayi negatif mi pozitif mi
s = int(input("Bir sayi gir: "))
negPoz = s > 0
print(f"Girilen sayi pozitif: {negPoz}")

