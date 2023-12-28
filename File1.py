t = float(input())
if t < 15.5:
    print(" ХОЛОДНО ")
elif t > 28:
    print(" ЖАРКО ")
else:
    print(" НОРМАЛЬНО ")


n = int(input())
c = False
for i in range(n):
    a = input()
    if "Кот" in a or "кот" in a:
        c = True
        break
if c:
    print(" МЯУ ")
else:
    print(" НЕТ ")


slova = input()
minx = slova
maxx = slova
y = "ДА"
n = "НЕТ"
while True:
    slova = input()
    if slova == "стоп":
        if len(set(minx)) - set(maxx()) == 0:
            print(n)
            braek
        else:
            print(n)
            break
        if len(slova) > len(maxx):
            maxx = slova
        if len(slova) < len(minx):
            minx = slova
