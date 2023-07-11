name, surname, age, job = 'Elif', 'Gültekin', 21, 'mühendis'

#Yukarıdaki değişkenlerle 'Benim adım Elif Gültekin, yaşım 21 ve mesleğim mühendis.' yazdır.
print(f"Benim adım {name} {surname}, yaşım {str(age)} ve mesleğim {job}.")
print("Benim adım {} {}, yaşım {} ve mesleğim {}." .format(name, surname, age, job))
result = "Benim adım "+ name+ " "+ surname+ ", yaşım "+ str(age)+ " ve mesleğim "+ job+ "."
print(result)

# 'Hello world' ifadesindeki w harfini W ile değiştir.
s = 'Hello world'
s= s[:6] + 'W' + s[-4:]
print(s)

# 'abc' ifadesini yanyana üç kere yazdır.
s= 'abc'*3
print(s)