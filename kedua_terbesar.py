def runner_up(*numbers):
    numbers = sorted(numbers)
    return numbers[-2]

user_input = input("Masukkan angka-angka (pisahkan dengan spasi): ")
numbers = [int(angka) for angka in user_input.split()] # Menciptakan list dari user input dan mengubahnya menjadi int
result = runner_up(*numbers)
print(f'Runner-upNya adalah {result}')