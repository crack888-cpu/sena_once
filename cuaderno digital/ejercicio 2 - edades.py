edad = int(input("Ingresar edad: "))
if edad > 13 and edad < 18:
    print("Tu edad está entre 13 y 18 años")
elif edad <= 13:
    print("Tu edad es menor o igual a 13 años")
else:
    print("Eres mayor de edad")