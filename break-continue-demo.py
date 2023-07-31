# 1-100 arası tek sayıların toplamı

i = 0
toplam = 0

while (i <= 100):
    i += 1
    if ( i % 2 == 0):
        continue
    toplam += i
print(f"Toplam: {toplam}")
