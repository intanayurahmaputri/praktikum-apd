def data():
    suhu = ['suhu_1', 'suhu_2', 'suhu_3', 'suhu_4', 'suhu_5', 'suhu_6']

    suhu[0] = float(27)
    suhu[1] = float(33)
    suhu[2] = float(46)
    suhu[3] = float(55)
    suhu[4] = float(67)
    suhu[5] = float(92)
    
    print("Tampilkan 46°C hingga 92°C: ", suhu[-4: ])

    suhu1F = (9 / 5) * suhu[0] + 32
    suhu2F = (9 / 5) * suhu[1] + 32
    suhu3K = suhu[2] + 273.15
    suhu4K = suhu[3] + 273.15
    suhu5R = (4 / 5) * suhu[4]
    suhu6R = (4 / 5) * suhu[5]
    
    jumlah = suhu1F + suhu2F + suhu3K + suhu4K + suhu5R + suhu6R
    print("Jumlah: " + str(jumlah))
    
    rata2 = jumlah / 6
    print("Rata-rata: " + str(rata2))
    
    NIM = 62

    nimBandingRerata = NIM < rata2
    print("Pernyataan perbandingan NIM < rata-rata bernilai: " + str(nimBandingRerata))
data()