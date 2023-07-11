# yarıçapı verilen ve pi= 3.14 olan dairenin alanı ve çevresi
pi = 3.14
r = input("yari cap: ") 
r= float(r)
alan = pi * (r**2)
cevre = 2*pi*r

print("Alan: ", alan)
print("Cevre: ", cevre)

alan = str(alan)
cevre = str(cevre)

print("Alan: "+ alan + " Çevre: "+ cevre)