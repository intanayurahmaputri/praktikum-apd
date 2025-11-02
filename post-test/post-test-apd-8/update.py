def ubahDataTeman(teman, nomor, nama, telp, hobi, musik):
    if nomor not in teman:
        raise KeyError("Nomor teman tidak ditemukan")

    teman[nomor]['nama'] = nama
    teman[nomor]['telp'] = telp
    teman[nomor]['hobi'] = hobi
    teman[nomor]['genreMusik'] = musik
    return teman

def ubahUsername(akun, username_baru):
    akun['admin']['username'] = username_baru
    return akun

def ubahPassword(akun, password_baru):
    akun['admin']['password'] = password_baru
    return akun