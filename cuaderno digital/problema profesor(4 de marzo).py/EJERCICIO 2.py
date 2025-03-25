empleados = {
    "Juan": 3500,
    "Maria": 4200,
    "Pedro": 2800,
    "Ana": 3900}

suma = 0
for i in empleados:
    suma += empleados[i]
print(f"Salario promedio: {suma/len(empleados)}")