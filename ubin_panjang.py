def u(ubin1, ubin5, panjang):
# cek apakah seluruh ubin kalau digabungkan cukup untuk menutupi semua panjangnya?
    if panjang <= (ubin1 * 1 + ubin5 * 5):
        # panjang total semua ubin bisa... berarti kemungkinan bisa
        # apakah cukup dengan ubin 5 saja?
        if (panjang // 5) <= ubin5 and (panjang % 5 == 0):
            print('Bisa')
        elif (panjang % 5) <= ubin1:
            print('Bisa')
        else:
            print('Tidak bisa, karena ubin 5 melebihi panjang dan ubin 1 tidak mencukupi.')
    else:
        print('Tidak bisa, karena semua ubin yang digabungkan tetap tidak cukup untuk panjang.')

ubin1 = int(input('Masukkan jumlah ubin 1: '))
ubin5 = int(input('Masukkan jumlah ubin 5: '))
panjang = int(input('Masukkan panjang lantainya: '))

print(u(ubin1, ubin5, panjang))