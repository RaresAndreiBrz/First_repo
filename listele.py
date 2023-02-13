#sortati lista 2 dupa penultimu caracter din fiecare string din lista
#numarti cate elem sunt intr o lista mai mult decat o data, cu elim spatiilor, litera mare , si semne punctuatie
#lista metode , utlizarea lor.
#extrage din lista mare "_",ultimul 6, extragem 2 din mijloc
#display john and his email only if his status active is true
#ceraza un dict mai complex cu date primitive pt key, pt valori: lista de dict cu tuple set si liste
data_type = " "
if data_type == "lista":
    lista_1 = [1, 2, 3, 4, 5, 6]
    lista_2 = ["apple", "mac", "iphone", "ipad", "apple"]
    lista_3 = [1, True, "_", False, 5.2 ]
    print(lista_1[0], lista_1[2])
    x = lista_1.reverse()
    print(lista_1)
    print(x)
    lista_1.sort()
    print(lista_1)
    lista_2.sort()
    print(lista_2)

    print(lista_2.count("apple"))

    y = (lista_1 + lista_2)
    print(y)

    x = ["a", "b", "c", "d"]
    y = x.copy()
    u = x[:]
    y[0] = "E"
    print(x, y, u)
    print(id(x), id(y), id(o), id(u))


    lista_matrice = [lista_1, lista_2, lista_3]
    print(lista_matrice)

    lista_mare = [lista_matrice, [0, 1, lista_1, ["a","b", "c"], [lista_matrice]], {}, True]
    print(lista_mare)
    print(lista_mare[0])
    print(lista_mare[0][0])
    print(lista_mare[0][0][-1])
elif data_type == "set":
    #SET
    print("SETURI")
    my_set = {2, 3, 4, 5, 6, 7, 2, 3, 4, 5, 6, 7}
    print(my_set)
    my_list = [ 1, 1, 1, 1, 1, 1,]
    second_set = {1, 2, 3, 8, 20, 5, 7}
    print(my_set.difference(second_set), my_list.intersection(second_set))
    second_set.difference(_update(my_set))
elif data_type == "tuple":
    print("TUPLURI")
    #TUPLES
    tuple = (1,2,5,7)
    print(tuple[0], tuple[-1])
    tuple[0] = 7
    print(tupla)
    print(type(tuple))
    a = (1, )
    print(type(a))
    print(a[:])
elif data_type == "dictionary":
    dictionar = {
        "user1" : "admin",
        "user2" : "Petre",
        "user3": {
            "name" : "John",
            "email" : "john@john.com",
            "isActive" : True
        }
    }
    print(dictionar["user2"], dictionar["user3"]["email"])

#Live 1
lista_1 = [1, 2, 3, 4, 5, 6]
lista_2 = ["apple", "mac", "iphone", "ipad", "apple"]
lista_3 = [1, True, "_", False, 5.2 ]
lista_matrice = [lista_1, lista_2, lista_3]
lista_mare = [lista_matrice, [0, 1, lista_1, ["a","b", "c"], [lista_matrice]], {}, True]

#sortati lista 2 dupa penultimu caracter din fiecare string din lista
lista_2.sort(key=lambda x: x[-2])
print(lista_2)

#numarti cate elem sunt intr o lista mai mult decat o data, cu elim spatiilor, litera mare , si semne punctuatie
numaratoare1 = lista_2.count("apple")
print(numaratoare1)
from collections import Counter
numaratoare2 = Counter(lista_matrice)
print(numaratoare2)
#numaratoare litere mari
print("Litere mari: " + sum(1 for c in lista_mare if c.isupper()))

