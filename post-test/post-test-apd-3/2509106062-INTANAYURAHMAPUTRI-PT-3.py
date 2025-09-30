# Masuk Akun
print("Mau masuk? Isi dulu username dan passwordnya.")
namaPanggilan = "Aya"
tigaDigitTerakhirNIM = "062"

username = (str(input("Masukkan username Anda: ")))
password = (str(input("Masukkan password Anda: ")))

if username == namaPanggilan and password == tigaDigitTerakhirNIM:
    print("Username benar dan password benar, berhasil masuk. Silakan kerjakan tugas konversi.")
    
    # Konversi Panjang
    print("Pertama, kerjakan konversi panjang.")
    feet = float(input("Masukkan ukuran satuan panjang kaki: "))
    km = float(input("Masukkan ukuran satuan panjang kilometer: "))
    cm = float(input("Masukkan ukuran satuan panjang sentimeter: "))
    
    feetToM = feet * 0.3048
    kmToM = km * 1000
    cmToM = cm / 100
    
    print(f"Hasil konversi ukuran dari satuan panjang kaki ke satuan panjang meter adalah {feetToM} meter.")
    print(f"Hasil konversi ukuran dari satuan panjang kilometer ke satuan panjang meter adalah {kmToM} meter.")
    print(f"Hasil konversi ukuran dari satuan panjang sentimeter ke satuan panjang meter adalah {cmToM} meter.")
    
    # Konversi Massa
    print("Kedua, kerjakan konversi massa.")
    pound = float(input("Masukkan ukuran satuan massa pon: "))
    ton = float(input("Masukkan ukuran satuan massa ton: "))
    gram = float(input("Masukkan ukuran satuan massa gram: "))
    cg = float(input("Masukkan ukuran satuan massa sentigram: "))
    mg = float(input("Masukkan ukuran satuan massa miligram: "))
    
    poundToKilogram = pound * 0.45359237
    tonToKilogram = ton * 1000
    gramToKilogram = gram / 1000
    cgToKilogram = cg * 0.00001
    mgToKilogram = mg * 0.000001
    
    print(f"Hasil konversi ukuran dari satuan massa pon ke satuan massa kilogram adalah {poundToKilogram} kilogram.")
    print(f"Hasil konversi ukuran dari satuan massa ton ke satuan massa kilogram adalah {tonToKilogram} kilogram.")
    print(f"Hasil konversi ukuran dari satuan massa gram ke satuan massa kilogram adalah {gramToKilogram} kilogram.")
    print(f"Hasil konversi ukuran dari satuan massa sentigram ke satuan massa kilogram adalah {cgToKilogram} kilogram.")
    print(f"Hasil konversi ukuran dari satuan massa miligram ke satuan massa kilogram adalah {mgToKilogram} kilogram.")
    
    # Konversi Suhu
    print("Ketiga, kerjakan konversi suhu.")
    celcius = float(input("Masukkan ukuran satuan suhu celcius: "))
    fahrenheit = float(input("Masukkan ukuran satuan suhu fahrenheit: "))
    reamur = float(input("Masukkan ukuran satuan suhu reamur: "))
    
    celciusToKelvin = celcius + 273.15
    fahrenheitToKelvin = (((fahrenheit - 32) * 5) / 9) + 273.15
    reamurToKelvin = (reamur * (5 / 4)) + 273.15
    
    print(f"Hasil konversi ukuran dari satuan suhu celcius ke satuan suhu kelvin adalah {celciusToKelvin} K.")
    print(f"Hasil konversi ukuran dari satuan suhu fahrenheit ke satuan suhu kelvin adalah {fahrenheitToKelvin} K.")
    print(f"Hasil konversi ukuran dari satuan suhu reamur ke satuan suhu kelvin adalah {reamurToKelvin} K.")
    
    # Konversi Waktu
    print("Keempat, kerjakan konversi waktu.")
    menit = float(input("Masukkan ukuran satuan waktu menit: "))
    jam = float(input("Masukkan ukuran satuan waktu jam: "))
    
    menitKeDetik = menit * 60
    jamKeDetik = jam * 3600
    
    print(f"Hasil konversi waktu dari satuan waktu menit ke satuan waktu detik adalah {menitKeDetik} detik.")
    print(f"Hasil konversi waktu dari satuan waktu jam ke satuan waktu detik adalah {jamKeDetik} detik.")
    
    # Konversi Mata Uang
    print("Kelima, kerjakan konversi mata uang.")
    IDR = float(input("Masukkan nominal uang Rupiah: "))
    USD = float(input("Masukkan nominal uang Dolar AS: "))
    GBP = float(input("Masukkan nominal uang Poundsterling: "))
    EUR = float(input("Masukkan nominal uang Euro: "))
    
    IDRtoUSD = IDR / 16000
    USDtoIDR = USD * 16000
    
    print(f"Hasil konversi mata uang dari Rupiah ke Dolar AS adalah US$ {IDRtoUSD}.")
    print(f"Hasil konversi mata uang dari Dolar AS ke Rupiah adalah Rp {USDtoIDR}.")
    
    EURtoUSD = EUR * 1.1
    USDtoEUR = USD / 1.1
    
    print(f"Hasil konversi mata uang dari Euro ke Dolar AS adalah US$ {EURtoUSD}.")
    print(f"Hasil konversi mata uang dari Dolar AS ke Euro adalah € {USDtoEUR}.")
    
    GBPtoIDR = GBP * 20000
    IDRtoGBP = IDR / 20000
    
    print(f"Hasil konversi mata uang dari Poundsterling ke Rupiah adalah Rp {GBPtoIDR}.")
    print(f"Hasil konversi mata uang dari Rupiah ke Poundsterling adalah £ {IDRtoGBP}.")
    
    # Tugas Selesai
    print("Tugas telah selesai dikerjakan.")
    
    kumpul = str(input("Kumpul?: "))
    jawaban1 = "Ya, kumpulkan."
    
    if kumpul == jawaban1:
        print("Selamat! Tugas telah berhasil dikumpulkan.")
    else:
        print("Tugas batal dikumpulkan, jangan lupa kumpul tugas dan perhatikan tenggat waktu.")
        
elif username != namaPanggilan and password == tigaDigitTerakhirNIM:
    print("Username salah dan password benar. Coba lagi.")
    
elif username == namaPanggilan and password != tigaDigitTerakhirNIM:
    print("Username benar dan password salah. Coba lagi.")
    
else:
    print("Akun tidak ditemukan. Coba lagi.")