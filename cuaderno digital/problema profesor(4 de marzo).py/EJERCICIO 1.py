
lista = [5, 3.2, 7, 3.2, 12, 5, 8.5, 7, 10, 15, 3.2, 12, 7, 20, 8.5, 5, 10,3.2, 15, 20]
dict = {}

for dato in lista:
    if dato in dict:
        dict[dato] += 1
    else:
        dict[dato] = 1

print(dict)
