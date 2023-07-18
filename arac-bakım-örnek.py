# 1. Bakım => 1. yıl
# 2. Bakım => 2. yıl
# 3. Bakım => 3. yıl
import datetime 

tarih = input(" Aracınız hangi tarihte trafiğe çıktı? (yyyy/aa/gg): ")
tarih = tarih.split('/')
trafigeCikis = datetime.datetime(int(tarih[0]), int(tarih[1]), int(tarih[2]))

simdi = datetime.datetime.now()
fark = simdi - trafigeCikis
day = fark.days

print(f"Araç {day} gündür trafikte")
if day <= 365:
    print("1. servis aralığı")
elif day > 365 and day <= 365*2:
    print("2. servis aralığı")
elif day > 365*2 and day <= 365*3:
    print("3. servis aralığı")
else:
    print("Hatalı bilgi")

