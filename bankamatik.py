
hesap1 = {
    'ad': 'Elif Gültekin',
    'hesapNo': '123',
    'bakiye': 3000,
    'kredi': 2000 
}

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}, {hesap['hesapNo']} nolu hesabinizda {hesap['bakiye']} TL bakiye ve {hesap['kredi']} TL kredi bulunmaktadir.")

    if (hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar
        print("Paranizi cekebilirsiniz.")
    else:
        toplam = hesap['bakiye'] + hesap['kredi']

        if (toplam >= miktar):
            krediCek = input("Kredi cekmek ister misiniz?(e/h): ")

            if krediCek == 'e':
             krediMiktar = miktar - hesap['bakiye']
             hesap['bakiye'] = 0
             hesap['kredi'] -= krediMiktar

             print("Paranizi cekebilirsiniz.")
            else:
               print(f"Yetersiz bakiye")

        else:
          print(f"Yetersiz bakiye")
             

def bakiyeSorgula(hesap):
  print(f"{hesap['hesapNo']} nolu hesabinizda {hesap['bakiye']} TL bakiye ve {hesap['kredi']} TL kredi bulunmaktadir.")

paraCek(hesap1, 3000)
paraCek(hesap1, 2000)
bakiyeSorgula(hesap1)
