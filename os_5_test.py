max_ramm = 64000
razdel = int(input("Введите кол-во разделов "))
razmer_razdela = max_ramm // razdel
razdels = []
zadachi = []
min_zadachi = []
for i in range(1, razdel):
    razdels.append(max_ramm//razdel)
razdels.append(max_ramm//razdel + max_ramm % razdel)

print("Введите размер задачи для каждого раздела:")
z = 0
ostatok = 0
for x in range(razdel):
    print(razdels[z])
    test_zadacha = int(input())
    if test_zadacha > razdels[z]:
        ostatok = test_zadacha - razdels[z]
        zadachi.append(test_zadacha - ostatok)
    else:
        test_zadacha += ostatok
        zadachi.append(test_zadacha)
    z += 1
    if test_zadacha > max_ramm:
        print("Превыщен обьем памяти")
        break
v = 0
if ostatok > 0:
    min_point = min(zadachi)
    plus_point = min_point + ostatok
    min(zadachi) == plus_point
    ostatok -= ostatok

print(razdels)
print(zadachi, sum(zadachi))
print(ostatok)

