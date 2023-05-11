def cek_digit_kanan(bil1, bil2, bil3):
    digit_kanan1 = bil1 % 10
    digit_kanan2 = bil2 % 10
    digit_kanan3 = bil3 % 10
    
    if digit_kanan1 == digit_kanan2 == digit_kanan3:
        print('Semua digit paling kanan dari ketiga bilangan sama')
    elif digit_kanan1 == digit_kanan2 != digit_kanan3:
        print(f'Digit paling kanan bilangan {bil1} dan {bil2} sama, sedangkan digit paling kanan bilangan {bil3} beda sendiri.')
    elif digit_kanan1 == digit_kanan3 != digit_kanan2:
        print(f'Digit paling kanan bilangan {bil1} dan {bil3} sama, sedangkan digit paling kanan bilangan {bil2} beda sendiri.')
    elif digit_kanan2 == digit_kanan3 != digit_kanan1:
        print(f'Digit paling kanan bilangan {bil2} dan {bil3} sama, sedangkan digit paling kanan bilangan {bil1} beda sendiri.')
    else:
        print('Semua digit paling kanan tidak sama')

bil1 = int(input('Masukkan bilangan pertama: '))
bil2 = int(input('Masukkan bilangan kedua: '))
bil3 = int(input('Masukkan bilangan ketiga: '))

print(cek_digit_kanan(bil1, bil2, bil3))