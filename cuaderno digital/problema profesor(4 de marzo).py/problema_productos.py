cant = int(input("Ingresa la cantidad de productos: "))
lista = []
i = 0
while i < cant:
    nombre = str(input(f"Nombre del producto {i + 1}: "))
    lista.append(nombre)
print(f"LIsta de productos: {lista}")