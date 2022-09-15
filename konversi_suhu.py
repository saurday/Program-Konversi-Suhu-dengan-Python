#Nama : Nisaur Rohmah
#NIM  : 220441100141

print ("\nPROGRAM KONVERSI SUHU\n")

indeks = {
    "Celcius    ": "c",
    "Reamur     ": "r",
    "Fahrenheit ": "f",
    "Kelvin     ": "k",

}
for i in indeks:
    print("Skala suhu : ", i, "\t Indeks : ", indeks[i])
suhu = float(input("Masukkan Suhu : "))
skala = input("Masukkan indeks satuan skala suhu : ")

if (skala == "c"):
    print(suhu, "derajat celcius : ")
    print("Reamur       = ", (suhu*4/5), "derajat ")
    print("Fahrenheit   = ", (suhu*9/5)+32, "derajat  ")
    print("Kelvin       = ", suhu + 273, "derajat  ")
elif (skala == "r"):
    print(suhu, "derajat reamur : ")
    print("Celcius       = ", (suhu*5/4), "derajat ")
    print("Fahrenheit    = ", (suhu*9/4)+32, "derajat  ")
    print("Kelvin        = ", suhu*5/4+ 273, "derajat  ")
elif (skala == "f"):
    print(suhu, "derajat fahrenheit : ")
    print("Celcius       = ", (5/9)*(suhu-32), "derajat ")
    print("Reamur        = ", (4/9)*(suhu-32), "derajat  ")
    print("Kelvin        = ", (5/9)*(suhu-32)+273, "derajat  ")
elif (skala == "k"):
    print(suhu, "derajat kelvin : ")
    print("Celcius       = ", suhu-273, "derajat ")
    print("Reamur        = ", (4/5 * (suhu-273)), "derajat  ")
    print("Fahrenheit    = ", ((9/5)*(suhu-273) +32), "derajat  ")