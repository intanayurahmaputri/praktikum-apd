from read import tampilTeman
from create import tambahTeman
from delete import hapusTeman

def menuPengguna(username, daftarTemanPengguna, clearScreen, jeda, inquirer, keluarAplikasi):
    if username not in daftarTemanPengguna:
        daftarTemanPengguna[username] = {}
        
    while True:
        clearScreen()
        print(f"=== MENU PENGGUNA: {username} ===\n")
        
        pengguna_questions = [
            inquirer.List('menu',
                message="Pilih Menu ₍^. .^₎⟆",
                choices=[
                    'Lihat data teman',
                    'Tambah teman',
                    'Hapus teman',
                    'Keluar akun',
                    'Keluar aplikasi'
                ],
            ),
        ]
        
        answers = inquirer.prompt(pengguna_questions)
        fitur = answers['menu']
        
        try:
            if fitur == 'Lihat data teman':
                clearScreen()
                tampilTeman(daftarTemanPengguna[username])
                
            elif fitur == 'Tambah teman':
                clearScreen()
                print("=== TAMBAH TEMAN BARU ===\n")
                teman_questions = [
                    inquirer.Text('nama', message="Nama", validate=lambda _, x: len(x) > 0),
                    inquirer.Text('telp', message="Nomor telepon", validate=lambda _, x: len(x) > 0),
                    inquirer.Text('hobi', message="Hobi", validate=lambda _, x: len(x) > 0),
                    inquirer.Text('genreMusik', message="Genre musik", validate=lambda _, x: len(x)> 0)
                ]
                teman_answers = inquirer.prompt(teman_questions)
                if teman_answers:
                    daftarTemanPengguna[username] = tambahTeman(
                        daftarTemanPengguna[username], 
                        teman_answers['nama'], 
                        teman_answers['telp'],
                        teman_answers['hobi'],
                        teman_answers['genreMusik'])
                    print("\nTeman baru berhasil ditambahkan! ૮꒰ ˶• ༝ •˶꒱ა ♡")
                
            elif fitur == 'Hapus teman':
                clearScreen()
                if not daftarTemanPengguna[username]:
                    print("Belum ada data teman. ૮◞ ‸ ◟ ა")
                else:
                    tampilTeman(daftarTemanPengguna[username])
                    print()
                    hapus_question = [
                        inquirer.Text('nomor',
                            message="Nomor teman yang ingin dihapus",
                            validate=lambda _, x: x.isdigit() and int(x) in daftarTemanPengguna[username]
                        )
                    ]
                    hapus_answer = inquirer.prompt(hapus_question)
                    if hapus_answer:
                        hapus = int(hapus_answer['nomor'])
                        daftarTemanPengguna[username] = hapusTeman(daftarTemanPengguna[username], hapus)
                        print("\nTeman berhasil dihapus! ૮꒰ ˶• ༝ •˶꒱ა ♡")
                        
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
        
    return daftarTemanPengguna