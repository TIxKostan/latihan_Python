def nama_terpanjang(nama1, nama2, nama3):
    
    panjang1 = len(nama1)
    panjang2 = len(nama2)
    panjang3 = len(nama3)

    if panjang1 > panjang2 and panjang1 > panjang3:
        print(f'Nama terpanjang dari ketiga nama tersebut adalah {nama1}')
    elif panjang2 > panjang1 and panjang2 > panjang3:
        print(f'Nama terpanjang dari ketiga nama tersebut adalah {nama2}')
    else:
        print(f'Nama terpanjang dari ketiga nama tersebut adalah {nama3}')

nama1 = input('Masukkan nama 1: ')
nama2 = input('Masukkan nama 2: ')
nama3 = input('Masukkan nama 3: ')

print(nama_terpanjang(nama1, nama2, nama3))