import os
import time
import inquirer

from autentikasi import login
from admin_menu import menuAdmin
from user_menu import menuPengguna

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

def intro():
    clearScreen()
    print("Selamat datang di Telechan (˶˃ ᵕ ˂˶) .ᐟ.ᐟ")
    print()
    print("♡ ♥ ♡ Loading... ♡ ♥ ♡".center(38))
    jeda()

def keluarAplikasi():
    clearScreen()
    print("Terima kasih telah menggunakan Telechan. Sampai jumpa lagi! ꉂ(˵˃ ᗜ ˂˵)")
    jeda()
    exit()

def main():
    global temanAdmin
    daftarTemanPengguna = {'aya': temanPengguna}
    akun = {
        'admin': {'username': 'admin', 'password': 'admin123'},
        'pengguna': [
            {'username': 'aya', 'password': 'aya123'}
        ]
    }

    while True:
        clearScreen()
        print("=== MAIN MENU ===\n")
        questions = [
            inquirer.List('menu',
                message="Pilih Menu ₍^. .^₎⟆",
                choices=['Masuk ke akun', 'Keluar aplikasi'],
            ),
        ]
        answers = inquirer.prompt(questions)
        pilihan = answers['menu']

        if pilihan == 'Keluar aplikasi':
            keluarAplikasi()

        elif pilihan == 'Masuk ke akun':
            role, username = login(akun, clearScreen, jeda, inquirer)
            if role == 'admin':
                temanAdmin, akun = menuAdmin(temanAdmin, akun, clearScreen, jeda, inquirer, keluarAplikasi)
            elif role == 'pengguna':
                daftarTemanPengguna = menuPengguna(username, daftarTemanPengguna, clearScreen, jeda, inquirer, keluarAplikasi)

intro()
main()