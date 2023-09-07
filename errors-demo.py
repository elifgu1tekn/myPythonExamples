liste = ["1", "2", "5a", "10b", "abc", "10", "50"]
# Liste elemanlarının içindeki ayısal değerleri bul
for x in liste:
    try:
       result = int(x)
       print(result)
    except ValueError:
       continue

# Kullanıcı 'q' girmedikçe aldığın her inputun sayı olduğundan emin ol, aksi halde hata mesajı ver
while True:
   sayi = input('sayi: ')
   if sayi == 'q':
      break
   try:
      result = float(sayi)
      print(f"Girdiğiniz sayi: {result}")
      break
   except ValueError:
      print("Geçersiz sayi")
      continue
   
# Girilen parola içinde türkçe karakter hatası ver
def checkPassword(parola):
   turkce_karakter = 'şçğüöıİ'

   for i in parola:
      if i in turkce_karakter:
         raise TypeError('Parola türkçe karakter içeremez.')
      else:
         pass
   print('geçerli parola')

parola = input('parola: ')

try:
   checkPassword(parola)
except TypeError as err:
   print(err) 

# Faktöriyel fonksiyonu oluşturup fonksiyona gelen değer için hata mesajları ver
def faktoriyel(x):
   x = int(x)

   if x<0:
      raise ValueError('Negatif deger')
   
   result = 1

   for i in range(1, x+1):
      result *= i

   return result

for x in [5, 10, 20, -3, '10a']:
   try:
      y = faktoriyel(x)
   except ValueError as err:
      print(err)
      continue
   print(y)
