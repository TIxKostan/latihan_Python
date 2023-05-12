# dictionary version
'''
def jumlah_hari_dalam_bulan(month):
    nama_bulan = {
        1: 'Januari',
        2: 'Februari',
        3: 'Maret',
        4: 'April',
        5: 'Mei',
        6: 'Juni',
        7: 'Juli',
        8: 'Agustus',
        9: 'September',
        10: 'Oktober',
        11: 'November',
        12: 'Desember'
    }
    jumlah_hari = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30 ,31]
    if 1 <= month <= 12:
        print(f'Jumlah hari dalam bulan {nama_bulan[month]} adalah {jumlah_hari[month-1]}')
    else:
        print('Bulan tidak ada di kalendar')
'''

# ternary operator version
def jumlah_hari_dalam_bulan(bulan):
    jumlah_hari = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30 ,31]
    print(f'Jumlah hari dalam bulan januari ada {jumlah_hari[0]}') if bulan == 1 else print(f'Jumlah hari dalam bulan februari ada {jumlah_hari[1]}') if bulan == 2 else print(f'Jumlah hari dalam bulan maret ada {jumlah_hari[2]}') if bulan == 3 else print(f'Jumlah hari dalam bulan april ada {jumlah_hari[3]}') if bulan == 4 else print(f'Jumlah hari dalam bulan mei ada {jumlah_hari[4]}') if bulan == 5 else print(f'Jumlah hari dalam bulan juni ada {jumlah_hari[5]}') if bulan == 6 else print(f'Jumlah hari dalam bulan juli ada {jumlah_hari[6]}') if bulan == 7 else print(f'Jumlah hari dalam bulan agustus ada {jumlah_hari[7]}') if bulan == 8 else print(f'Jumlah hari dalam bulan september ada {jumlah_hari[8]}') if bulan == 9 else print(f'Jumlah hari dalam bulan oktober ada {jumlah_hari[9]}') if bulan == 10 else print(f'Jumlah hari dalam bulan november ada {jumlah_hari[10]}') if bulan == 11 else print(f'Jumlah hari dalam bulan desember ada {jumlah_hari[11]}') if bulan == 12 else print('Bulan tidak ada di kalendar')

bulan = int(input('Masukkan bulan yang anda ingin ketahui jumlah harinya: '))

jumlah_hari_dalam_bulan(bulan)

'''
Penjelasan

kalau mau yang jelas pakai dictionary version karena source code-nya terlihat jelas,
sedangkan source code ternary operator version mungkin terlihat lebih pendek tapi saya tidak sarankan untuk kasus yang panjang (soalnya cape ketiknya dan tidak kelihatan jelas source code-nya).
'''