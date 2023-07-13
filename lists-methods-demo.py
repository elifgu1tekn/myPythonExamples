names = ['Ali', 'Yağmur', 'Hakan','Deniz']
years = [1998, 2000, 1998, 1987]

# names in sonuna 'Cenk' ekle
names.append('Cenk')
print(names)

# names in başına 'Sena' ekle
names.insert(0, 'Sena')
print(names)

# 'Deniz' in indeksi 
index = names.index('Deniz')
print(index)

# 'Deniz' i listeden sil
names.pop(4)  # or names.remove('Deniz')
print(names)

# 'Ali' listenin elemanı mı?
result = 'Ali' in names
print(result)

# names elemanlarını ters çevir
names.reverse()
print(names)

# names elamanlarını alfabetik sırala
names.sort()
print(names)

# years ı küçükten büyüğe sırala
years.sort()
print(years)

# years ın en büyük ve en küçük elemanı
val1 = min(years)
val2 = max(years)
print(f"Min: {val1} Max: {val2}")

# years dizisinde kaç tane 1998 var?
val = years.count(1998)
print(val)

# years ın tüm elemanlarını sil
years.clear()
print(years)
