# if else normal version
'''
def positif_negatif(n):
    if n > 0:
        print(f'{n} adalah bilangan positif')
    elif n < 0:
        print(f'{n} adalah bilangan negatif')
    else:
        print(n)
'''

# ternary operation version
def positif_negatif(n):
    print(f'{n} adalah bilangan positif') if n > 0 else print(f'{n} adalah bilangan negatif') if n < 0 else print(f'{0}')
   
Bilangan = int(input('Masukkan sebuah bilangan: '))

print(positif_negatif(Bilangan))

'''
Penjelasan
Ternary operator (value if condition else value)

jadi python akan print(n adalah positif) if n > 0 else python akan print(n adalah negatif) if n < 0 else print(n adalah 0)
dibaca pelan-pelan aja gess
'''
