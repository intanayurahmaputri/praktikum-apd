import os
import time

akun = {
    'pengguna': {'username': 'aya', 'password': 'aya123'},
    'admin': {'username': 'admin', 'password': 'admin123'}
}

temanAdmin = {
    1: {'nama': 'zayneSnow', 'telp': '0825xxxxxxx1', 'hobi': 'Journaling', 'genreMusik': 'Screamo'},
    2: {'nama': 'stayrusCrow', 'telp': '0822xxxxxxx2', 'hobi': 'Night ride', 'genreMusik': 'Classic'},
    3: {'nama': 'calebApple', 'telp': '0821xxxxxxx3', 'hobi': 'Otomotif', 'genreMusik': 'Pop-Rock'},
    4: {'nama': 'rafayelFish', 'telp': '0896xxxxxxx4', 'hobi': 'Melukis', 'genreMusik': 'Indie-Rock'},
    5: {'nama': 'xavierStar', 'telp': '0895xxxxxxx5', 'hobi': 'Membaca', 'genreMusik': 'Vocaloid'}
}

temanPengguna = {
    1: {'nama': 'lavsRein', 'telp': '0896xxxxxxx1', 'hobi': 'Mobile Legends', 'genreMusik': 'EDM'},
    2: {'nama': 'hiroseNana', 'telp': '0821xxxxxxx2', 'hobi': 'Roblox', 'genreMusik': 'Pop'},
    3: {'nama': 'aluNada', 'telp': '0822xxxxxxx3', 'hobi': 'Memancing', 'genreMusik': 'Indie'},
    4: {'nama': 'vianNara', 'telp': '0823xxxxxxx4', 'hobi': 'Bermain futsal', 'genreMusik': 'Punk'}
}

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def jeda():
    time.sleep(5)
    clearScreen()

def login(usn, pw):
    for role in akun:
        if usn == akun[role]['username'] and pw == akun[role]['password']:
            return role
    return None

def tambahTeman(teman, nama, telp, hobi, musik):
    nomorBaru = len(teman) + 1
    teman[nomorBaru] = {'nama': nama, 'telp': telp, 'hobi': hobi, 'genreMusik': musik}
    return teman

def intro():
    clearScreen()
    print("Selamat datang di Telechan (˶˃ ᵕ ˂˶) .ᐟ.ᐟ")
    print()
    print("♡ ♥ ♡ Loading... ♡ ♥ ♡".center(38))
    time.sleep(2)
    clearScreen()

def keluarAplikasi():
    clearScreen()
    print("Terima kasih telah menggunakan Telechan. Sampai jumpa lagi! ꉂ(˵˃ ᗜ ˂˵)")
    exit()

def headerTeman():
    print("\n╔════════════════════════════════════════════════════════════════════╗")
    print("║                    🌸 DAFTAR TEMAN TELECHAN 🌸                     ║")
    print("╚════════════════════════════════════════════════════════════════════╝\n")

def tampilTeman(teman, index=1):
    if index > len(teman):
        return
    data = teman[index]
    print(f"𑣲 Teman {index}\nNama: {data['nama']}\nNomor telepon: {data['telp']}\nHobi: {data['hobi']}\nGenre musik: {data['genreMusik']}")
    print()
    tampilTeman(teman, index + 1)

def mainMenu():
    while True:
        clearScreen()
        print("==== MENU UTAMA ====")
        print("1. Masuk ke akun")
        print("2. Keluar aplikasi\n")

        pilihan = input("Pilih menu: ")

        if pilihan == '2':
            keluarAplikasi()

        elif pilihan == '1':
            clearScreen()
            print("Silakan masuk ke akun Anda.\n")
            usn = input("Masukkan username: ")
            pw = input("Masukkan password: ")

            role = login(usn, pw)

            if role == 'admin':
                menuAdmin()
            elif role == 'pengguna':
                menuPengguna()
            else:
                print()
                print("Username atau password salah (｡•̀ ⤙ •́ ｡ꐦ) !!!")
                jeda()
        else:
            print()
            print("Pilihan tidak valid. ૮◞ ‸ ◟ ა")
            jeda()

def menuAdmin():
    global temanAdmin, akun
    while True:
        clearScreen()
        print("=== MENU ADMIN ===")
        print("1. Lihat data teman")
        print("2. Tambah teman")
        print("3. Ubah data teman")
        print("4. Hapus teman")
        print("5. Ubah password")
        print("6. Ubah username")
        print("7. Keluar akun")
        print("8. Keluar aplikasi\n")

        fitur = input("Pilih fitur: ")

        try:
            if fitur == '1':
                clearScreen()
                headerTeman()
                tampilTeman(temanAdmin)
                
            elif fitur == '2':
                clearScreen()
                nama = input("Nama: ")
                telp = input("Nomor telepon: ")
                hobi = input("Hobi: ")
                genreMusik = input("Genre musik: ")
                temanAdmin = tambahTeman(temanAdmin, nama, telp, hobi, genreMusik)
                print()
                print("Teman berhasil ditambahkan! ૮꒰ ˶• ༝ •˶꒱ა ♡")

            elif fitur == '3':
                clearScreen()
                ubah = int(input('Ubah data teman ke berapa: '))
                clearScreen()
                headerTeman()
                tampilTeman(temanAdmin)
                print("Masukkan data baru! ૮ ˶ᵔ ᵕ ᵔ˶ ა")
                if ubah in temanAdmin:
                    temanAdmin[ubah]['nama'] = input('Nama baru: ')
                    temanAdmin[ubah]['telp'] = input('Nomor baru: ')
                    temanAdmin[ubah]['hobi'] = input('Hobi baru: ')
                    temanAdmin[ubah]['genreMusik'] = input('Genre musik baru: ')
                    print()
                    print('Data teman berhasil diubah!')
                else:
                    print('Teman tidak ditemukan.')

            elif fitur == '4':
                clearScreen()
                if not temanAdmin:
                    print("Belum ada data teman. ૮◞ ‸ ◟ ა")
                else:
                    headerTeman()
                    tampilTeman(temanAdmin)
                    hapus = int(input("Nomor teman yang ingin dihapus: "))
                    if hapus in temanAdmin:
                        del temanAdmin[hapus]
                        temanAdmin = {i+1: v for i, v in enumerate(temanAdmin.values())}
                        print()
                        print("Teman berhasil dihapus! ૮꒰ ˶• ༝ •˶꒱ა ♡")
                    else:
                        print()
                        print("Nomor teman tidak ditemukan (｡•̀ ⤙ •́ ｡ꐦ) !!!")

            elif fitur == '5':
                clearScreen()
                akun['admin']['password'] = input("Masukkan password baru: ")
                print()
                print("Password admin berhasil diubah! ૮꒰ ˶• ༝ •˶꒱ა ♡")

            elif fitur == '6':
                clearScreen()
                akun['admin']['username'] = input("Masukkan username baru: ")
                print()
                print("Username admin berhasil diubah! ૮꒰ ˶• ༝ •˶꒱ა ♡")

            elif fitur == '7':
                break

            elif fitur == '8':
                keluarAplikasi()

            else:
                print("Pilihan tidak valid. ૮◞ ‸ ◟ ა")

        except KeyError:
            print("Nomor teman tidak ditemukan (｡•̀ ⤙ •́ ｡ꐦ) !!!")
        except ValueError:
            print("Masukkan angka yang benar (｡•̀ ⤙ •́ ｡ꐦ) !!!")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

        jeda()

def menuPengguna():
    global temanPengguna
    while True:
        clearScreen()
        print("=== MENU PENGGUNA ===")
        print("1. Lihat data teman")
        print("2. Tambah teman")
        print("3. Hapus teman")
        print("4. Keluar akun")
        print("5. Keluar aplikasi\n")

        fitur = input("Pilih fitur: ")

        try:
            if fitur == '1':
                clearScreen()
                headerTeman()
                tampilTeman(temanPengguna)

            elif fitur == '2':
                clearScreen()
                nama = input("Nama: ")
                telp = input("Nomor telepon: ")
                hobi = input("Hobi: ")
                genreMusik = input("Genre musik: ")
                temanPengguna = tambahTeman(temanPengguna, nama, telp, hobi, genreMusik)
                print()
                print("Teman baru berhasil ditambahkan! ૮꒰ ˶• ༝ •˶꒱ა ♡")

            elif fitur == '3':
                clearScreen()
                if not temanPengguna:
                    print("Belum ada data teman. ૮◞ ‸ ◟ ა")
                else:
                    headerTeman()
                    tampilTeman(temanPengguna)
                    hapus = int(input("Nomor teman yang ingin dihapus: "))
                    if hapus in temanPengguna:
                        del temanPengguna[hapus]
                        temanPengguna = {i+1: v for i, v in enumerate(temanPengguna.values())}
                        print()
                        print("Teman berhasil dihapus! ૮꒰ ˶• ༝ •˶꒱ა ♡")
                    else:
                        print()
                        print("Nomor teman tidak ditemukan (｡•̀ ⤙ •́ ｡ꐦ) !!!")

            elif fitur == '4':
                break

            elif fitur == '5':
                keluarAplikasi()

            else:
                print("Pilihan tidak valid. ૮◞ ‸ ◟ ა")

        except KeyError:
            print("Nomor teman tidak ditemukan (｡•̀ ⤙ •́ ｡ꐦ) !!!")
        except ValueError:
            print("Masukkan angka yang benar (｡•̀ ⤙ •́ ｡ꐦ) !!!")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

        jeda()

intro()
mainMenu()