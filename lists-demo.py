cars = ["BMW", "Mercedes", "Opel", "Mazda"]
print(len(cars))

# Listenin ilk ve son elemanı
print(cars[0])
print(cars[3])

# Mazda'yı Toyota ile değiştir.
cars[3] = 'Toyota'
print(cars)

# Mercedes listenin elemanı mı?
a = 'Mercedes' in cars
print(a)

# Listenin -2 indeksindeki eleman
print(cars[-2])

# Listenin ilk 3 elemanı
print(cars[:3])

# Listenin son 2 elemanını 'Toyota' ve 'Renault' ile değiştir
cars[2]= 'Toyota'
cars[3]= 'Renault'
print(cars)

# Listeye 'Audi' ve 'Nissan' ekle
carsNew = cars + ['Audi', 'Nissan']
print(carsNew)

# Oluşan listenin son elemanını sil
del carsNew[-1]
print(carsNew)

# Listenin elemanlarını tersten yazdır

carsNew = carsNew[::-1]
print(carsNew)

print(20*'*')

# studentA: Yiğit Bilg 2010, (70,60,70)
# studentB: Sena Turan 1999, (80,80,70)
# studentC: Ahmet Turan 1998, (80,70,90)
# Yukarıdaki verileri bir liste içinde sakla

studentA = ['Yiğit', 'Bilgi', 2010, [70,60,70]]
studentB = ['Sena', 'Turan', 1999, [80,80,70]]
studentC = ['Ahmet', 'Turan', 1998, [80,70,90]]
student = [studentA, studentB, studentC]
print(student)

result = f"{studentA[0]} {studentA[1]} {2023-studentA[2]} yaşında ve not ortalaması {(studentA[3][0]+studentA[3][1]+studentA[3][2])/3}"
print(result)