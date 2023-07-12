website = "htpp://www.elifgu1tekn.com"
repositories = "myPythonExamples"

# ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini sil.
result = ' Hello World '.strip()

# "htpp://www.elifgu1tekn.com" içindeki elifgu1tekn hariç tüm karakterleri sil.
result = website.lstrip('.www//:ppth').rstrip('.com')

# 'repositories' karakter dizisinin içindeki tüm karakterleri küçük harf yap.
result = repositories.lower()

# 'website' içinde kaç tane e harfi var?
result = website.count('e')

# 'website' www ile başlayıp com ile bitiyor mu?
result = website.startswith('www')
result = website.endswith('com')

#'website' içinde .com ifadesi var mı?
result = website.find('.com')

# 'repositories' içindeki karakterlerin hepsi alfabetik mi?
result = repositories.isalpha()
result = repositories.isdigit()

# 'Contens' ifadesini stırda 50 karakter içine yerleştirip sağ ve soluna * ekle.
result = 'Contens'.center(50, "*")

# 'Hello World' dizsinin 'World' ifadesini 'There' olarak değiştir.
result = 'Hello World'.replace('World','There')

print(result)