# 0-24 => 0
# 25-44 => 1
# 45-54 => 2
# 55-69 => 3
# 70-84 => 4
# 85-100 => 5 

yazili1 = int(input("1. yazili notu: "))
yazili2 = int(input("2. yazili notu: "))
sozlu = int(input("Sözlü notu: "))
ort = (yazili1 + yazili2 + sozlu)/3

print(f"Not ortalası: {ort}")

if ort >= 0 and ort <= 24:
    print("Başarı durumu: 0")
elif ort >= 25 and ort <= 44:
    print("Başarı durumu: 1")
elif ort >= 45 and ort <= 54:
    print("Başarı durumu: 2")
elif ort >= 55 and ort <= 69:
    print("Başarı durumu: 3")
elif ort >= 70 and ort <= 84:
    print("Başarı durumu: 4")
elif ort >= 85 and ort <= 100:
    print("Başarı durumu: 5")

