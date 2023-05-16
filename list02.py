data = []
for i in range(1, 11):
    if i == 4:
        continue
    data.append(i)
data.insert(3, 4)
data.insert(10, 11)

print(data)