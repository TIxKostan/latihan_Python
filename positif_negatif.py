def positif_negatif(n):
    if n > 0:
        print(f'{n} adalah bilangan positif')
    elif n < 0:
        print(f'{n} adalah bilangan negatif')
    else:
        print(n)
    
Bilangan = int(input('Masukkan sebuah bilangan: '))

print(positif_negatif(Bilangan))
