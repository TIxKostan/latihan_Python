def suhu_suhu(suhu):
    if suhu == 36 or suhu == 37:
        print(f'suhu badan anda{suhu} derajat celcius ini adalah suhu normal manusia.')
    elif suhu > 32 and suhu < 35:
        print(f'suhu badan anda {suhu} derajat celcius anda Hipotermia ringan.')
    elif suhu >= 28 and suhu <= 32:
        print(f'suhu badan anda {suhu} derajat celcius anda Hipotermia sedang.')
    elif suhu < 28:
        print(f'suhu badan anda {suhu} derajat celcius anda Hipotermia berat.')
    elif suhu > 37 and suhu < 39:
        print(f'suhu badan anda {suhu} derajat celcius anda Demam.')
    elif suhu >= 40 and suhu < 45:
        print(f'suhu badan anda {suhu} derajat celcius anda Hipertermia (Overheating).')
    else:
        print("Anda sudah mati")

suhu = int(input('Berapa suhu badan anda:'))

print(suhu_suhu(suhu))