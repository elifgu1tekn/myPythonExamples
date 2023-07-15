x, y, z = 2, 5, 107
numbers = 1,5,7,10,6

# Kullanıcıdan alınan 2 sayının çarpımı ile x,y,z toplamının farkı
s1 = int(input("1. sayi: "))
s2= int(input("2. sayi: "))
carpim = s1* s2
print(f"2 sayinin carpimi: {carpim}")
toplam = x + y + z
print(f"x, y, z toplami: {toplam}")
fark = carpim - toplam
print(f"SONUC: {fark}")

# s1 = int(input("1. sayi: "))
#s2= int(input("2. sayi: "))
# result = (a*b) - (x+y+z)
#print(result)

# y'nin x'e kalansız bölümü
kalBol = y // x
print(kalBol)

# (x,y,z) toplamının mod 3'ü
mod = (x + y + z) % 3
print(mod)

# y'nin x. kuvveti
y **= x
print(y)

# x, *y, z = numbers işlemine göre z'nin küpü
x, *y, z = numbers 
z = z**3
print(z)

#  x, *y, z = numbers işlemine göre y'nin değerlerinin toplamı
x, *y, z = numbers 
toplam = y[0] + y[1] + y[2]
print(toplam)