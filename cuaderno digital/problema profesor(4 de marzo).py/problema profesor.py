cant = int(input("Ingresa numero estudiantes: "))
lista = []
i = 0
while i < cant:
    nombre = str(input(f"Nombre del estudiante {i + 1}: "))
    lista.append(nombre)
print(f"LIsta de estudiantes: {lista}")