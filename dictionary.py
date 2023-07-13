students = {}
number = input("Öğrenci no ")
name = input("Öğrenci adı: ")
surname = input("Öğrenci soyadı: ")
phone = input("Öğrenci telefon: ")

# students[number] = {
#  'name': name,
#  'surname': surname,
#  'phone': phone
# }

students.update({
    number: {
        'name': name,
        'surname': surname,
        'phone': phone
    }
})

print(students)


#Öğrenci numarası verilen bir öğrencinin bilgilerini yazdırma

ogrNo = input("Öğrenci no: ")
ogrenci = students[ogrNo]
print(f"Aradığınız {ogrNo} nolu öğrencinin adı {ogrenci['name']} soyadı {ogrenci['surname']} ve telefon numarası {ogrenci['phone']}")