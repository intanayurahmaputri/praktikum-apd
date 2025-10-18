import os
import time

os.system('cls')
print('Semangat ngodingnya (˶˃ ᵕ ˂˶) .ᐟ.ᐟ')
print('♡ ♥ ♡ Loading... ♡ ♥ ♡')
time.sleep(3)
os.system('cls')

akun = {
    'pengguna': {'username': 'aya', 'password': 'aya123'},
    'admin': {'username': 'admin', 'password': 'admin123'}
}

while True:
    os.system('cls')
    print('Selamat datang di Telechan! ₍^. .^₎⟆\n')
    print('1. Masuk ke akun')
    print('2. Keluar dari aplikasi\n')

    pilihan = input('Pilih menu: ')
    os.system('cls')

    if pilihan == '2':
        print('Terima kasih telah menggunakan Telechan. Sampai jumpa lagi!')
        break

    elif pilihan == '1':
        print('Silahkan masukkan akun Anda.\n')
        usn = input('Masukkan username: ')
        pw = input('Masukkan password: ')
        os.system('cls')

        login_berhasil = ''
        for i in akun:
            if usn == akun[i]['username'] and pw == akun[i]['password']:
                login_berhasil = i
                break

        if login_berhasil == '':
            print('Akun tidak ditemukan. Periksa kembali username dan password Anda.')
            time.sleep(3)
            continue

        if login_berhasil == 'admin':
            print(f"@{usn} berhasil masuk sebagai admin! Selamat menikmati fitur pro!")
            time.sleep(2)
            os.system('cls')

            teman = {
                1: {'nama': 'zayneSnow', 'telp': '0825xxxxxxx1', 'hobi': 'Journaling', 'musik': 'Screamo'},
                2: {'nama': 'stayrusCrow', 'telp': '0822xxxxxxx2', 'hobi': 'Night ride', 'musik': 'Classic'},
                3: {'nama': 'calebApple', 'telp': '0821xxxxxxx3', 'hobi': 'Otomotif', 'musik': 'Pop-Rock'},
                4: {'nama': 'rafayelFish', 'telp': '0896xxxxxxx4', 'hobi': 'Melukis', 'musik': 'Indie-Rock'},
                5: {'nama': 'xavierStar', 'telp': '0895xxxxxxx5', 'hobi': 'Membaca', 'musik': 'Vocaloid'}
            }

            while True:
                print('========== MENU ADMIN ==========')
                print('1. Lihat data teman')
                print('2. Ubah data teman')
                print('3. Hapus teman')
                print('4. Tambah teman')
                print('5. Ubah username/password admin')
                print('6. Keluar dari akun')
                print('7. Keluar dari aplikasi\n')

                fitur = input('Pilih fitur: ')
                os.system('cls')

                if fitur == '1':
                    for i in teman:
                        data = teman[i]
                        print(f"Teman {i}:")
                        print(f"Nama: {data['nama']}")
                        print(f"Nomor telepon: {data['telp']}")
                        print(f"Hobi: {data['hobi']}")
                        print(f"Genre musik: {data['musik']}\n")

                elif fitur == '2':
                    ubah = int(input('Ubah data teman ke berapa: '))
                    if ubah in teman:
                        teman[ubah]['nama'] = input('Nama baru: ')
                        teman[ubah]['telp'] = input('Nomor baru: ')
                        teman[ubah]['hobi'] = input('Hobi baru: ')
                        teman[ubah]['musik'] = input('Genre musik baru: ')
                        print('Data teman berhasil diubah!')
                    else:
                        print('Teman tidak ditemukan.')

                elif fitur == '3':
                    hapus = int(input('Pilih teman yang ingin dihapus: '))
                    if hapus in teman:
                        del teman[hapus]
                        print('Teman berhasil dihapus!')
                        temanBaru = {}
                        nomor = 1
                        for i in teman:
                            temanBaru[nomor] = teman[i]
                            nomor += 1
                        teman = temanBaru
                    else:
                        print('Nomor teman tidak ditemukan.')

                elif fitur == '4':
                    nama = input('Masukkan nama: ')
                    no = input('Masukkan nomor telepon: ')
                    hobi = input('Masukkan hobi: ')
                    musik = input('Masukkan genre musik: ')
                    nomorBaru = len(teman) + 1
                    teman[nomorBaru] = {'nama': nama, 'telp': no, 'hobi': hobi, 'musik': musik}
                    print('Teman baru berhasil ditambahkan!')

                elif fitur == '5':
                    usnBaru = input('Masukkan username baru: ')
                    pwBaru = input('Masukkan password baru: ')
                    akun['admin']['username'] = usnBaru
                    akun['admin']['password'] = pwBaru
                    print('Username dan password admin berhasil diubah!')

                elif fitur == '6':
                    print('Keluar akun berhasil! Kembali ke halaman login...')
                    time.sleep(2)
                    break

                elif fitur == '7':
                    print('Terima kasih telah menggunakan Telechan. Sampai jumpa lagi!')
                    exit()

                else:
                    print('Pilihan tidak valid.')

                time.sleep(5)
                os.system('cls')

        else:
            print(f"@{usn} berhasil masuk!")
            time.sleep(2)
            os.system('cls')

            teman = {
                1: {'nama': 'lavsRein', 'telp': '0896xxxxxxx1', 'hobi': 'Bermain Mobile Legends', 'musik': 'EDM'},
                2: {'nama': 'hiroseNana', 'telp': '0821xxxxxxx2', 'hobi': 'Bermain Roblox', 'musik': 'Pop'},
                3: {'nama': 'aluNada', 'telp': '0822xxxxxxx3', 'hobi': 'Memancing', 'musik': 'Indie'},
                4: {'nama': 'vianNara', 'telp': '0823xxxxxxx4', 'hobi': 'Bermain futsal', 'musik': 'Punk'}
            }

            while True:
                print('==== MENU PENGGUNA ====')
                print('1. Lihat data teman')
                print('2. Hapus teman')
                print('3. Tambah teman')
                print('4. Keluar dari akun')
                print('5. Keluar dari aplikasi\n')

                fitur = input('Pilih fitur: ')
                os.system('cls')

                if fitur == '1':
                    for i in teman:
                        data = teman[i]
                        print(f"Teman {i}:")
                        print(f"Nama: {data['nama']}")
                        print(f"Nomor telepon: {data['telp']}")
                        print(f"Hobi: {data['hobi']}")
                        print(f"Genre musik: {data['musik']}\n")

                elif fitur == '2':
                    hapus = int(input('Pilih teman yang ingin dihapus: '))
                    if hapus in teman:
                        del teman[hapus]
                        print('Teman berhasil dihapus!')
                        temanBaru = {}
                        nomor = 1
                        for i in teman:
                            temanBaru[nomor] = teman[i]
                            nomor += 1
                        teman = temanBaru
                    else:
                        print('Nomor teman tidak ditemukan.')

                elif fitur == '3':
                    nama = input('Masukkan nama: ')
                    no = input('Masukkan nomor telepon: ')
                    hobi = input('Masukkan hobi: ')
                    musik = input('Masukkan genre musik: ')
                    nomorBaru = len(teman) + 1
                    teman[nomorBaru] = {'nama': nama, 'telp': no, 'hobi': hobi, 'musik': musik}
                    print('Teman baru berhasil ditambahkan!')

                elif fitur == '4':
                    print('Keluar akun berhasil! Kembali ke halaman login...')
                    time.sleep(2)
                    break

                elif fitur == '5':
                    print('Terima kasih telah menggunakan Telechan. Sampai jumpa lagi!')
                    exit()

                else:
                    print('Pilihan tidak valid.')

                time.sleep(5)
                os.system('cls')

    else:
        print('Pilihan tidak valid.')
        time.sleep(2)