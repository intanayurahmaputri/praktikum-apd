# Masuk Ke Akun
namaPanggilan = "Aya"
tigaDigitTerakhirNIM = "062"

usn = str(input("Masukkan username Anda: "))
pw = str(input("Masukkan password Anda: "))

while usn == "" or pw == "":
    print("Username atau password tidak boleh kosong, silakan coba lagi.")
    usn = str(input("Masukkan username Anda: "))
    pw = str(input("Masukkan password Anda: "))

while usn != namaPanggilan and pw != tigaDigitTerakhirNIM:
    print("Username atau password Anda salah, silakan coba lagi.")
    usn = str(input("Masukkan username Anda: "))
    pw = str(input("Masukkan password Anda: "))

# Kantong Darah yang Ditampung
while True:
    goldar = str(input("Masukkan golongan darah yang dibutuhkan: "))

    if goldar == "A":
        Rh = str(input("Masukkan rhesus golongan darah A: "))
        if Rh == "+":
            print("Rhesus merupakan +, sehingga golongan darah menjadi A+.")
        else:
            print("Rhesus merupakan -, sehingga golongan darah menjadi A-.")
    elif goldar == "B":
        Rh = str(input("Masukkan rhesus golongan darah B: "))
        if Rh == "+":
            print("Rhesus merupakan +, sehingga golongan darah menjadi B+.")
        else:
            print("Rhesus merupakan -, sehingga golongan darah menjadi B-.")
    elif goldar == "AB":
        Rh = str(input("Masukkan rhesus golongan darah AB: "))
        if Rh == "+":
            print("Rhesus merupakan +, sehingga golongan darah menjadi AB+.")
        else:
            print("Rhesus merupakan -, sehingga golongan darah menjadi AB-.")
    elif goldar == "O":
        Rh = str(input("Masukkan rhesus golongan darah O: "))
        if Rh == "+":
            print("Rhesus merupakan +, sehingga golongan darah menjadi O+.")
        else:
            print("Rhesus merupakan -, sehingga golongan darah menjadi O-.")
    else:
        print("Golongan darah tidak boleh kosong, silakan coba lagi.")
        continue

    ulang = input("Apakah Anda masih mau input lagi? (Ya/Tidak): ")
    if ulang == "Ya":
        continue
    else:
        kantongDarah1 = int(input("Masukkan jumlah kantong darah A yang telah ditampung: "))
        kantongDarah2 = int(input("Masukkan jumlah kantong darah B yang telah ditampung: "))
        kantongDarah3 = int(input("Masukkan jumlah kantong darah AB yang telah ditampung: "))
        kantongDarah4 = int(input("Masukkan jumlah kantong darah O yang telah ditampung: "))

        konversi1 = kantongDarah1 * 500
        konversi2 = kantongDarah2 * 500
        konversi3 = kantongDarah3 * 500
        konversi4 = kantongDarah4 * 500
        
        jumlah = (konversi1 + konversi2 + konversi3 + konversi4)
        print(f"Total darah yang telah ditampung adalah {jumlah} ml.")
        break