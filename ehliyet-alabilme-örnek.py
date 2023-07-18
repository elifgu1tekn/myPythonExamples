# Ehliyet alma koşulu en az 18 yaş ve eğitim durumu lise veya üniversite olmalı
ad = input("Adinizi girin: ")
yas = int(input("Yasinizi girin: "))
egitim = input("Egitim seviyesi girin (ortaokul, lise vb. şekilde): ")

if (yas >= 18):
   if(egitim == 'lise' or egitim == 'üniversite'):
    print("Ehliyet alabilirsiniz.")
   else:
      print("Ehliyet ALAMAZSINIZ. Eğitim durumunuz yetersiz.")
else:
    print("Ehliyet ALAMAZSINIZ. Yaşınız tutmuyor.")
