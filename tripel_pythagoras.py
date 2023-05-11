def cek(a, b, c):
    conditions = [
    a ** 2 + b ** 2 == c ** 2,
    b ** 2 + c ** 2 == a ** 2,
    c ** 2 + a ** 2 == b ** 2
    ]
    for condition in conditions:
        if condition: # Jika salah satu kondisi terpenuhi maka True
            return True
    return False
    
a = int(input('Masukkan a: '))
b = int(input('Masukkan b: '))
c = int(input('Masukkan c: '))

if cek(a, b, c):
    print(f'\n jadi {a}, {b}, dan {c} adalah triple pythagoras.')
else:
    print(f'\nJadi {a}, {b}, dan {c} bukan triple pythagoras.')