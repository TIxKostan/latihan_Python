Reamur = lambda r: 0.8 * r
Fahrenheit = lambda f: (9/5) * f + 32
Kelvin = lambda k: k + 273.15

Celcius = int(input('Input C: '))

print(f'{Celcius} Celcius ke Reamur = {Reamur(Celcius)}')
print(f'{Celcius} Celcius ke Farenheit = {Fahrenheit(Celcius)}')
print(f'{Celcius} Celcius ke Kelvin = {Kelvin(Celcius)}')