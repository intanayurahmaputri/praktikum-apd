from prettytable import PrettyTable

def tampilTeman(teman, index=1, table=None):
    if table is None:
        table = PrettyTable()
        table.field_names = ["Teman", "Nama", "Nomor Telepon", "Hobi", "Genre Musik"]
        
    if index > len(teman):
        print(table)
        return
    
    data = teman[index]
    table.add_row([index, data['nama'], data['telp'], data['hobi'], data['genreMusik']])
    tampilTeman(teman, index + 1, table)