def a_b_c(a, b, c):    
    total = 0
    if a != b and a != c and b != c:
        total = a + b + c
    # jika semua sama
    elif a == b and a == c and b == c:
        total = 0
    elif a == b:
        total = c
    elif a == c:
        total = b
    else:
        total = a
    return total

a = int(input('Masukkan a: '))
b = int(input('Masukkan b: '))
c = int(input('Masukkan c: '))

print(a_b_c(a,b,c))
