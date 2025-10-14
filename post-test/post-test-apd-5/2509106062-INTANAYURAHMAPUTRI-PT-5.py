import os
import time

os.system('cls')
print('Semangat ngodingnya, Aya (˶˃ ᵕ ˂˶) .ᐟ.ᐟ')
print('♡ ♥ ♡ Loading... ♡ ♥ ♡')
time.sleep(3)
os.system('cls')


print('Selamat datang di Telechan! ₍^. .^₎⟆')
print(' ')

while True:
    akunBiasa1 = ('ayesAvgAcc', 'AyeN1!')
    akunAdmin = ('ayesProAcc', 'AyeN2!')
    akun = [akunBiasa1, akunAdmin]

    print('Silahkan masukkan akun Anda.')
    usn = input('Masukkan username: ')
    pw = input('Masukkan password: ')
    
    if usn == akun[0][0] and pw == akun[0][1]:
        print('@' + akun[0][0], 'berhasil masuk sebagai pengguna biasa!')
        os.system('cls')
        print('Fitur Yang Tersedia:\n1. Melihat data teman\n2. Menghapus teman\n3. Menambah teman\n4. Mengganti akun')
        print(' ')
        
        # teman1
        nama1 = 'lavsRein'
        nomortelepon1 = '0896xxxxxxx1'
        hobi1 = 'Bermain Mobile Legends'
        genremusik1 = 'EDM'
        teman1 = [[nama1, nomortelepon1], [hobi1, genremusik1]]
        
        # teman2
        nama2 = 'hiroseNana'
        nomortelepon2 = '0821xxxxxxx2'
        hobi2 = 'Bermain Roblox'
        genremusik2 = 'Pop'
        teman2 = [[nama2, nomortelepon2], [hobi2, genremusik2]]
        
        # teman3
        nama3 = 'aluNada'
        nomortelepon3 = '0822xxxxxxx3'
        hobi3 = 'Memancing'
        genremusik3 = 'Indie'
        teman3 = [[nama3, nomortelepon3], [hobi3, genremusik3]]
        
        # teman4
        nama4 = 'vianNara'
        nomortelepon4 = '0823xxxxxxx4'
        hobi4 = 'Bermain futsal'
        genremusik4 = 'Punk'
        teman4 = [[nama4, nomortelepon4], [hobi4, genremusik4]]
        
        teman = [teman1, teman2, teman3, teman4]
        
        fitur = int(input('Mau pakai fitur yang mana? (1/2/3/4): '))
        os.system('cls')
        
        if fitur == 1:    
            print('Data teman 1:\nNama:', teman1[0][0], '\nNomor telepon:', teman1[0][1], '\nHobi:', teman1[1][0], '\nGenre musik:', teman1[1][1])
            print(' ')
            print('Data teman 2:\nNama:', teman2[1][0], '\nNomor telepon:', teman2[1][1], '\nHobi:', teman2[1][0], '\nGenre musik:', teman2[1][1])
            print(' ')
            print('Data teman 3:\nNama:', teman3[0][0], '\nNomor telepon:', teman3[0][1], '\nHobi:', teman3[1][0], '\nGenre musik:', teman3[1][1])
            print(' ')
            print('Data teman 4:\nNama:', teman4[0][0], '\nNomor telepon:', teman4[0][1], '\nHobi:', teman4[1][0], '\nGenre musik:', teman4[1][1])
            break
        
        elif fitur == 3:
            namaBaru = input('Masukkan nama: ')
            noTelpBaru = input('Masukkan nomor telepon: ')
            hobiBaru = input('Masukkan hobi: ')
            genreMusikBaru = input('Masukkan genre musik: ')
            temanBaru = [[namaBaru, noTelpBaru], [hobiBaru, genreMusikBaru]]
            teman.append(temanBaru)
            print('Teman berhasil ditambahkan! Data teman baru:\nNama:', namaBaru, '\nNomor telepon:', noTelpBaru, '\nHobi:', hobiBaru, '\nGenre musik:', genreMusikBaru)
            print(' ')
            print(teman)
            break
            
            
        elif fitur == 4:
            continue
            
        elif fitur > 4:
            print('Pilihan tidak valid')
            break
        
        while fitur == 2:
            kontakHapus = input('Ingin menghapus teman yang mana? (1/2/3/4): ')
            os.system('cls')
            if kontakHapus == '1':
                del teman[0]
                print('Teman 1 berhasil dihapus.')
                print(teman)
                break
            elif kontakHapus == '2':
                del teman[1]
                print(' Teman 2 berhasil dihapus.')
                print(teman)
                break
            elif kontakHapus == '3':
                del teman[2]
                print('Teman 3berhasil dihapus.')
                print(teman)
                break
            elif kontakHapus == '4':
                del teman[3]
                print('Teman 4 berhasil dihapus.')
                print(teman)
                break
            else:
                print('Pilihan tidak valid.')
                time.sleep(3)
                os.system('cls')
            continue
        break
            
        
        
    elif usn == akun[1][0] and pw == akun[1][1]:
        print('@' + akun[1][0], 'berhasil masuk sebagai admin! Selamat menikmati fitur pro!')
        os.system('cls')
        print('Fitur Yang Tersedia:\n1. Melihat data teman\n2. Mengubah data teman\n3. Menghapus teman\n4. Menambah teman\n5. Mengubah username dan password\n6. Mengganti akun')
        print(' ')
        
        # teman 1
        nama1 = 'zayneSnow'
        nomortelepon1 = '0825xxxxxxx1'
        hobi1 = 'Journaling'
        genremusik1 = 'Screamo'
        teman1 = [[nama1, nomortelepon1], [hobi1, genremusik1]]
                
        # teman 2
        nama2 = 'stayrusCrow'
        nomortelepon2 = '0822xxxxxxx2'
        hobi2 = 'Night ride'
        genremusik2 = 'Classic'
        teman2 = [[nama2, nomortelepon2], [hobi2, genremusik2]]
                
        # teman 3
        nama3 = 'calebApple'
        nomortelepon3 = '0821xxxxxxx3'
        hobi3 = 'Otomotif'
        genremusik3 = 'Pop-Rock'
        teman3 = [[nama3, nomortelepon3], [hobi3, genremusik3]]
                
        # teman 4
        nama4 = 'rafayelFish'
        nomortelepon4 = '0896xxxxxxx4'
        hobi4 = 'Melukis'
        genremusik4 = 'Indie-Rock'
        teman4 = [[nama4, nomortelepon4], [hobi4, genremusik4]]
                
        # teman 5
        nama5 = 'xavierStar'
        nomortelepon5 = '0895xxxxxxx5'
        hobi5 = 'Membaca'
        genremusik5 = 'Vocaloid'
        teman5 = [[nama5, nomortelepon5], [hobi5, genremusik5]]
        
        teman = [teman1, teman2, teman3, teman4, teman5]
        
        fitur = int(input('Mau pakai fitur yang mana? (1/2/3/4/5/6): '))
        os.system('cls')
        
        if fitur == 1:
            print('Data teman 1:\nNama:', teman1[0][0], '\nNomor telepon:', teman1[0][1], '\nHobi:', teman1[1][0], '\nGenre musik:', teman1[1][1])
            print(' ')
            print('Data teman 2:\nNama:', teman2[0][0], '\nNomor telepon:', teman2[0][1], '\nHobi:', teman2[1][0], '\nGenre musik:', teman2[1][1])
            print(' ')
            print('Data teman 3:\nNama:', teman3[0][0], '\nNomor telepon:', teman3[0][1], '\nHobi:', teman3[1][0], '\nGenre musik:', teman3[1][1])
            print(' ')
            print('Data teman 4:\nNama:', teman4[0][0], '\nNomor telepon:', teman4[0][1], '\nHobi:', teman4[1][0], '\nGenre musik:', teman4[1][1])
            print(' ')
            print('Data teman 5:\nNama:', teman5[0][0], '\nNomor telepon:', teman5[0][1], '\nHobi:', teman5[1][0], '\nGenre musik:', teman5[1][1])
            break
            
        elif fitur == 2:
            os.system('cls')
            temanUbah = input('Ingin mengubah data teman yang mana? (1/2/3/4/5): ')
            os.system('cls')
            if temanUbah == '1':
                namaBaru = input('Masukkan nama baru: ')
                noTelpBaru = input('Masukkan nomor telepon baru: ')
                hobiBaru = input('Masukkan hobi baru: ')
                genreMusikBaru = input('Masukkan genre musik baru: ')
                nama1 = namaBaru
                nomortelepon1 = noTelpBaru
                hobi1 = hobiBaru
                genremusik1 = genreMusikBaru
                teman1 = [namaBaru, noTelpBaru, hobiBaru, genreMusikBaru]
                teman[0] = teman1
                print(' ')
                print('Data teman 1 berhasil diubah!')
                print('Nama:', nama1, '\nNomor telepon:', nomortelepon1, '\nHobi:', hobi1, '\nGenre musik:', genremusik1)
            elif temanUbah == '2':
                namaBaru = input('Masukkan nama baru: ')
                noTelpBaru = input('Masukkan nomor telepon baru: ')
                hobiBaru = input('Masukkan hobi baru: ')
                genreMusikBaru = input('Masukkan genre musik baru: ')
                nama2 = namaBaru
                nomortelepon2 = noTelpBaru
                hobi2 = hobiBaru
                genremusik2 = genreMusikBaru
                teman2 = [namaBaru, noTelpBaru, hobiBaru, genreMusikBaru]
                teman[1] = teman2
                print(' ')
                print('Data teman 2 berhasil diubah!')
                print('Nama:', nama2, '\nNomor telepon:', nomortelepon2, '\nHobi:', hobi2, '\nGenre musik:', genremusik2)
            elif temanUbah == '3':
                namaBaru = input('Masukkan nama baru: ')
                noTelpBaru = input('Masukkan nomor telepon baru: ')
                hobiBaru = input('Masukkan hobi baru: ')
                genreMusikBaru = input('Masukkan genre musik baru: ')
                nama3 = namaBaru
                nomortelepon3 = noTelpBaru
                hobi3 = hobiBaru
                genremusik3 = genreMusikBaru
                teman3 = [namaBaru, noTelpBaru, hobiBaru, genreMusikBaru]
                teman[2] = teman3
                print(' ')
                print('Data teman 3 berhasil diubah!')
                print('Nama:', nama3, '\nNomor telepon:', nomortelepon3, '\nHobi:', hobi3, '\nGenre musik:', genremusik3)
            elif temanUbah == '4':
                namaBaru = input('Masukkan nama baru: ')
                noTelpBaru = input('Masukkan nomor telepon baru: ')
                hobiBaru = input('Masukkan hobi baru: ')
                genreMusikBaru = input('Masukkan genre musik baru: ')
                nama4 = namaBaru
                nomortelepon4 = noTelpBaru
                hobi4 = hobiBaru
                genremusik4 = genreMusikBaru
                teman4 = [namaBaru, noTelpBaru, hobiBaru, genreMusikBaru]
                teman[3] = teman4
                print(' ')
                print('Data teman 4 berhasil diubah!')
                print('Nama:', nama4, '\nNomor telepon:', nomortelepon4, '\nHobi:', hobi4, '\nGenre musik:', genremusik4)
            elif temanUbah == '5':
                namaBaru = input('Masukkan nama baru: ')
                noTelpBaru = input('Masukkan nomor telepon baru: ')
                hobiBaru = input('Masukkan hobi baru: ')
                genreMusikBaru = input('Masukkan genre musik baru: ')
                nama5 = namaBaru
                nomortelepon5 = noTelpBaru
                hobi5 = hobiBaru
                genremusik5 = genreMusikBaru
                teman5 = [namaBaru, noTelpBaru, hobiBaru, genreMusikBaru]
                teman[4] = teman5
                print(' ')
                print('Data teman 5 berhasil diubah!')
                print('Nama:', nama5, '\nNomor telepon:', nomortelepon5, '\nHobi:', hobi5, '\nGenre musik:', genremusik5)
            else:
                print('Pilihan tidak valid.')
            break
            
            
        elif fitur == 4:
            namaBaru = input('Masukkan nama: ')
            noTelpBaru = input('Masukkan nomor telepon: ')
            hobiBaru = input('Masukkan hobi: ')
            genreMusikBaru = input('Masukkan genre musik: ')
            temanBaru = [namaBaru, noTelpBaru, hobiBaru, genreMusikBaru]
            teman.append(temanBaru)
            print('Teman berhasil ditambahkan! Data teman baru:\nNama:', namaBaru, '\nNomor telepon:', noTelpBaru, '\nHobi:', hobiBaru, '\nGenre musik:', genreMusikBaru)
            print(' ')
            print(teman)
            break
            
            
        elif fitur == 5:
            ubahUsn = input('Ingin mengubah username dan password? (Ya?Tidak): ')
            os.system('cls')
            if ubahUsn == 'Ya':
                usnBaru = input('Masukkan username baru: ')
                if usnBaru == akun[0][0]:
                    print('Username sudah digunakan, silakan coba lagi.')
                elif usnBaru == akun[1][0]:
                    print('Username sudah digunakan, silakan coba lagi.')
                else:
                    akunBiasa1 = (usnBaru, pw)
                    akun[0] = akunBiasa1
                    print('Username berhasil diubah! Username baru Anda adalah @' + usnBaru)
            else:
                pass
            
            time.sleep(3)
            os.system('cls')
            ubahPw = input('Ingin mengubah password? (Ya/Tidak): ')
            os.system('cls')
            if ubahPw == 'Ya':
                pwBaru = input('Masukkan password baru: ')
                akunBiasa1 = (usnBaru, pwBaru)
                akun[0] = akunBiasa1
                print('Password berhasil diubah! Password baru Anda adalah ' + pwBaru)
                time.sleep(3)
                os.system('cls')
                print(akun)
            else:
                print('Batal mengubah username dan password.')
            break
            
            
        elif fitur == 6:
            continue
            
            
        elif fitur > 6:
            print('Pilihan tidak valid.')
            break
                
                
        while fitur == 3:
            kontakHapus = input('Ingin menghapus teman yang mana? (1/2/3/4/5): ')
            os.system('cls')
            if kontakHapus == '1':
                del teman[0]
                print('Teman 1 berhasil dihapus.')
                print(teman)
                break
            elif kontakHapus == '2':
                del teman[1]
                print(' Teman 2 berhasil dihapus.')
                print(teman)
                break
            elif kontakHapus == '3':
                del teman[2]
                print('Teman 3berhasil dihapus.')
                print(teman)
                break
            elif kontakHapus == '4':
                del teman[3]
                print('Teman 4 berhasil dihapus.')
                print(teman)
                break
            elif kontakHapus == '5':
                del teman[4]
                print('Teman 5 berhasil dihapus.')
                print(teman)
                break
            else:
                print('Pilihan tidak valid.')
                time.sleep(3)
                os.system('cls')
            continue
        break
    
    else:
        print('Akun tidak ditemukan. Periksa kembali username dan password Anda.')
        time.sleep(3)
        os.system('cls')
        continue