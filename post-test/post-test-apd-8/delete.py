def hapusTeman(teman, nomor):
    if nomor not in teman:
        raise KeyError("Nomor teman tidak ditemukan")
    
    del teman[nomor]
    return {i+1: v for i, v in enumerate(teman.values())}