def kamu_bekerja(gaji, jam_kerja):
    gaji_sebelum_pajak = gaji * jam_kerja
    print(f'Pendapatan Budi selama libur musim panas sebelum melakukan pembayaran pajak adalah Rp.{gaji_sebelum_pajak:,.0f}')
    bayar_pajak = (14/100) * gaji_sebelum_pajak
    gaji_setelah_pajak = gaji_sebelum_pajak - bayar_pajak
    print(f'Pendapatan Budi selama libur musim panas setelah melakukan pembayaran pajak adalah Rp.{gaji_setelah_pajak:,.0f}')
    beli_baju_aksesoris = (10/100) * gaji_setelah_pajak
    print(f'Kamu menghabiskan Rp.{beli_baju_aksesoris:,.0f} untuk beli baju dan aksesoris.')
    beli_alat_tulis = (1/100) * gaji_setelah_pajak
    print(f'Kamu menghabiskan Rp.{beli_alat_tulis:,.0f} untuk beli buku dan alat tulis.')
    uang_sisa_belanja = gaji_setelah_pajak - (beli_baju_aksesoris + beli_alat_tulis)
    uang_sedekah = (25/100) * uang_sisa_belanja
    print(f'Jumllah uang yang akan kamu sedekahkan sebanyak Rp.{uang_sedekah:,.0f}')
    uang_sedekah_anak_yatim = (30/100) * uang_sedekah
    print(f'Jumlah uang yang akan diterima anak yatim adalah sebesar Rp.{uang_sedekah_anak_yatim:,.0f} ')
    uang_sedekah_kaum_dhuafa = uang_sedekah - uang_sedekah_anak_yatim
    print(f'Jumlah uang yang akan diterima anak kaum dhuafa adalah sebesar Rp.{uang_sedekah_kaum_dhuafa:,.0f}')
    pass

gaji = int(input("Gaji anda per jam = "))
jam_kerja = int(input('Seminggu anda kerja berapa jam: '))

kamu_bekerja(gaji, jam_kerja)