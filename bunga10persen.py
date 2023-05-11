uang_erika = 200
target = 400
cuan = 0.1  # 10% dilambangkan dengan 0.1 dalam decimal
tahun = 0

while uang_erika < target:
    print(int(uang_erika))
    tahun = tahun + 1
    uang_erika += uang_erika * cuan

print(f"Butuh {tahun} tahun agar uang Erika mencapai {target} juta.")