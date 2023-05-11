def hitung_hari(sekarang, n):
    n = n % 7
    hari = ['senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu', 'minggu']
    indeks_sekarang = hari.index(sekarang) # Mengambil index (urutan dalam list) sekarang dari list variabel hari
    indeks_hari_baru = (indeks_sekarang + n) % 7
    hari_baru = hari[indeks_hari_baru] # Menyimpan index indeks_hari_baru_pada list hari
    print(hari_baru)

sekarang = input('Masukkan nama hari sekarang: ')
n = int(input('Mau berapa hari kedepan?: '))
hitung_hari(sekarang, n)