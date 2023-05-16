def max_value(data):
    return max(data)

def min_value(data):
    return min(data)

def avarage(data):
    return sum(data)/len(data)

n = int(input('Masukkan n: '))
data = []
for i in range (n):
    angka = int(input('Masukkan angka: '))
    data.append(angka)

maksimum = max_value(data)
print(f'\nnilai maksimum: {maksimum}')

minimum = min_value(data)
print(f'\nnilai minimum: {minimum}')

rata_rata = avarage(data)
print(f'\nnilai rata-rata: {rata_rata:.2f}')

print('Urut ascending:', end=' ')
data.sort()
print(data)
print('Urutan descending:', end=' ')
data.sort(reverse=True)
print(data)