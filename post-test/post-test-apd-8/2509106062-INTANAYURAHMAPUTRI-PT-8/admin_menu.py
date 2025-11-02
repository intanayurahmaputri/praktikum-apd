from read import tampilTeman
from create import tambahTeman
from delete import hapusTeman
from update import ubahDataTeman, ubahUsername, ubahPassword
import inquirer
from inquirer.errors import ValidationError

def menuAdmin(temanAdmin, akun, clearScreen, jeda, inquirer, keluarAplikasi):
    while True:
        clearScreen()
        print("=== MENU ADMIN ===\n")
        
        admin_questions = [
            inquirer.List('menu',
                message="Pilih Menu ₍^. .^₎⟆",
                choices=[
                    'Lihat data teman',
                    'Tambah teman',
                    'Ubah data teman',
                    'Hapus teman',
                    'Ubah password',
                    'Ubah username',
                    'Keluar akun',
                    'Keluar aplikasi'
                ],
            ),
        ]
        
        answers = inquirer.prompt(admin_questions)
        fitur = answers['menu']
        
        try:
            if fitur == 'Lihat data teman':
                clearScreen()
                tampilTeman(temanAdmin)
                
            elif fitur == 'Tambah teman':
                clearScreen()
                print("=== TAMBAH TEMAN BARU ===\n")
                teman_questions = [
                    inquirer.Text('nama', message="Nama", validate=lambda _, x: len(x) > 0),
                    inquirer.Text('telp', message="Nomor telepon", validate=lambda _, x: len(x) > 0),
                    inquirer.Text('hobi', message="Hobi", validate=lambda _, x: len(x) > 0),
                    inquirer.Text('genreMusik', message="Genre musik", validate=lambda _, x: len(x) > 0)
                ]
                teman_answers = inquirer.prompt(teman_questions)
                if teman_answers:
                    temanAdmin = tambahTeman(temanAdmin, 
                        teman_answers['nama'], 
                        teman_answers['telp'],
                        teman_answers['hobi'],
                        teman_answers['genreMusik'])
                    print("\nTeman berhasil ditambahkan! ૮꒰ ˶• ༝ •˶꒱ა ♡")
                
            elif fitur == 'Ubah data teman':
                clearScreen()
                if not temanAdmin:
                    print("Belum ada data teman. ૮◞ ‸ ◟ ა")
                else:
                    tampilTeman(temanAdmin)
                    print()

                    ubah_questions = [
                        inquirer.Text(
                            'nomor',
                            message="Nomor teman yang ingin diubah datanya",
                            validate=lambda _, x: x.isdigit() and int(x) in temanAdmin
                        )
                    ]
                    ubah_answers = inquirer.prompt(ubah_questions)

                    if ubah_answers:
                        ubah = int(ubah_answers['nomor'])
                        clearScreen()
                        tampilTeman(temanAdmin)
                        print("\nMasukkan data baru! ૮ ˶ᵔ ᵕ ᵔ˶ ა\n")

                        data_baru = [
                            inquirer.Text('nama', message="Nama baru", validate=lambda _, x: len(x) > 0),
                            inquirer.Text('telp', message="Nomor baru", validate=lambda _, x: len(x) > 0),
                            inquirer.Text('hobi', message="Hobi baru", validate=lambda _, x: len(x) > 0),
                            inquirer.Text('genreMusik', message="Genre musik baru", validate=lambda _, x: len(x) > 0)
                        ]
                        jawaban_baru = inquirer.prompt(data_baru)

                        if jawaban_baru:
                            temanAdmin = ubahDataTeman(
                                temanAdmin,
                                ubah,
                                jawaban_baru['nama'],
                                jawaban_baru['telp'],
                                jawaban_baru['hobi'],
                                jawaban_baru['genreMusik']
                            )
                            print('\nData teman berhasil diubah! ૮꒰ ˶• ༝ •˶꒱ა ♡')


            elif fitur == 'Hapus teman':
                clearScreen()
                if not temanAdmin:
                    print("Belum ada data teman. ૮◞ ‸ ◟ ა")
                else:
                    tampilTeman(temanAdmin)
                    print()
                    hapus_question = [
                        inquirer.Text('nomor',
                            message="Nomor teman yang ingin dihapus",
                            validate=lambda _, x: x.isdigit() and int(x) in temanAdmin
                        )
                    ]
                    hapus_answer = inquirer.prompt(hapus_question)
                    if hapus_answer:
                        hapus = int(hapus_answer['nomor'])
                        temanAdmin = hapusTeman(temanAdmin, hapus)
                        print("\nTeman berhasil dihapus! ૮꒰ ˶• ༝ •˶꒱ა ♡")
                        
            elif fitur == 'Ubah password':
                clearScreen()
                print("=== UBAH PASSWORD ===\n")
                pw_question = [
                    inquirer.Text('password',
                        message="Password admin baru",
                        validate=lambda _, x: len(x.strip()) > 0
                    )
                ]
                pw_answer = inquirer.prompt(pw_question)
                if pw_answer and pw_answer['password'].strip():
                    akun = ubahPassword(akun, pw_answer['password'].strip())
                    print("\nPassword admin berhasil diubah! ૮꒰ ˶• ༝ •˶꒱ა ♡")
                
            elif fitur == 'Ubah username':
                clearScreen()
                print("=== UBAH USERNAME ===\n")
                usn_question = [
                    inquirer.Text('username',
                        message="Username admin baru",
                        validate=lambda _, x: len(x.strip()) > 0
                    )
                ]
                usn_answer = inquirer.prompt(usn_question)
                if usn_answer and usn_answer['username'].strip():
                    akun = ubahUsername(akun, usn_answer['username'].strip())
                    print("\nUsername admin berhasil diubah! ૮꒰ ˶• ༝ •˶꒱ა ♡")
                
            elif fitur == 'Keluar akun':
                clearScreen()
                print("♡ ♥ ♡ Loading... ♡ ♥ ♡".center(38))
                jeda()
                break
                
            elif fitur == 'Keluar aplikasi':
                keluarAplikasi()
                
        except KeyError:
            print("\nNomor teman tidak ditemukan (｡•̀ ⤙ •́ ｡ꐦ) !!!")
        except ValueError:
            print("\nMasukkan angka yang benar (｡•̀ ⤙ •́ ｡ꐦ) !!!")
        except Exception as e:
            print(f"\nTerjadi kesalahan: {e}")
            
        jeda()
        
    return temanAdmin, akun