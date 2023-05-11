def tukar(a, b):
    temp = a
    a = b
    b = temp
    return a, b

a = int(input('a: '))
b = int(input('b: '))

print('\nsebelum ditukar')
print('a = ', a)
print('b = ', b)

a, b = tukar(a, b)

print('\nsetelah ditukar')
print('a = ', a)
print('b = ', b)