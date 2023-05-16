'''
tuple harus sepasang
read only
'''
data_laundry  = [
     # no, nama, transaksi terakhir (kg), transaksi terakhir (rp)
     (100, "Mang", 7, 28000),
    (120, 'Bambang', 5, 20000),
    (119, 'Agus', 2, 50000),
    (118, 'Wati', 1, 5000),
]

total = 0
for data in data_laundry:
    print(data[3])
    total = total + data[3]

print(f'total adalah Rp.{total}')

kilo = 0
for kg in data_laundry:
    print(kg[2])
    kilo = kilo + kg[2]

print(f'Mesin cuci kita sudah mencuci {kilo} kg pakaian')

data_laundry.sort(key=lambda x: x[3], reverse=True)
for pelangan in data_laundry:
    print(f'\n{pelangan[0]}, {pelangan[1]}\t Rp. {pelangan[3]}')
