sayi = int(input("Bir sayi gir: "))
asalMi = True
if sayi == 1:
    asalMi = False

for i in range(2,sayi):
    if (sayi % i == 0):
       asalMi = False
       break

if asalMi:
   print("Asal")
else:
   print("Asal değil")

