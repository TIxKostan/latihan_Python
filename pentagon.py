def pentagon(n):
    for i in range(1, n+1): # i + 1 sampai n
        bilangan = int(i * (3*i-1) / 2)
        print(bilangan, end=" ") # end=" " biar ada spasi antar output

print('Deret n bilangan pentagon')
n = int(input('\nMasukkan n: '))
pentagon(n)