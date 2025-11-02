def tambahTeman(teman, nama, telp, hobi, musik):
    nomorBaru = len(teman) + 1
    teman[nomorBaru] = {'nama': nama, 'telp': telp, 'hobi': hobi, 'genreMusik': musik}
    return teman