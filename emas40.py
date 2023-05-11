harga_emas_awal = 650000
beli_awal = harga_emas_awal * 25
harga_emas_sekarang = 685000
beli_kedua = harga_emas_sekarang * 15
harga_emas_naik = 715000
total = beli_awal + beli_kedua
keuntungan_pertama = (harga_emas_sekarang - harga_emas_awal) * 25
keuntungan_kedua = (harga_emas_naik * 40) - total
print(f'keuntungan pertama adalah Rp.{keuntungan_pertama}')
print(f'keuntungan setelah harga emas naik menjadi Rp.715.000 adalah Rp.{keuntungan_kedua}')