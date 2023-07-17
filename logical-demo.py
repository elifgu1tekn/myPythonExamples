# Girilen sayi 0-100 arasında mı?
sayi = float(input("sayi: "))
result = (sayi>0) and (sayi<=100)
print(f"Sayi 0-100 arasinda mi : {result}")

# Girilen sayi pozitif çift sayı mı?
result = (sayi>0) and (sayi%2==0)
print(f"Sayi pozitif cift sayi mi: {result}")

# Email ve parola ile giriş kontrolü
email = 'email@elif'
password = 'ab12'

girilenEmail = input("email: ")
girilenPassword = input("password: ")
result = (girilenEmail == email) and (girilenPassword == password)
print(f"Uygulamaya giris basarili mi: {result}")

# Kullanıcıdan 2 vize (%60) ve 1 final (%40) notu alıp ortalama hesapla. Eğer ort. 50 ve üstündeyse geçti.
# a) Ort. 50 olsa bile final en az 50 olmalı
vize1 = int(input("1. vize: "))
vize2 = int(input("2. vize: "))
final = int(input("final: "))
ort = ((vize1 + vize2)/2)*0.6 + (final*0.4)
result = (ort >=50) and (final>=50)

# b) Finalden 70+ aldığında ort önemsiz olsun
result = (ort >=50) or (final>=70) 

print(f"Ogrencinin ortalamasi: {ort} ve gecme durumu: {result}")
