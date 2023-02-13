import random
zar_ales = int(input("Ghiceste zarul selectand  un numar de la 1 la 6: "))
zar_random = random.choice([1, 2, 3, 4, 5, 6])
print(zar_random)
if zar_ales == zar_random:
    print("Felicitari.Ati ghicit numarul. ")
elif zar_ales > zar_random:
    print("Ai pierdut.Ati selectat un numar mai mare decat cel al zarului")
else:
    print("Ai pierdut.Ati selectat un numar mai mic decat cel al zarului.")