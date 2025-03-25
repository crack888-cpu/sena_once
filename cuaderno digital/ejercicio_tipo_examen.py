print("Programa médico")

edad = int(input("Ingresa tu edad: "))

while True:
    p, a, ps, pd = map(float, input("Ingresar valores (peso en KG, altura en M, presión sistólica Mmgh, presión diastólica Mmgh): ").split())
    if p > 0 and a > 0 and ps > 0 and pd > 0:
        break 
    print("Valores incorrectos. Por favor, ingresa valores correctos.")

fumador = str(input("Eres fumador SI/NO? ")).strip().lower()
imc = p / (a**2)

if imc < 18.5:
    print("Bajo de peso")
elif 18.5 <= imc < 25:
    print("Peso normal")
elif 25 <= imc < 30:
    print("Sobrepeso")
else:
    print("Obesidad")

if ps < 120 and pd < 80:
    print("Presión arterial normal")
elif 120 <= ps < 129 and pd < 80:
    print("Presión arterial elevada")
else: 
    print("Presión alta")

if imc >= 25 and ps >= 129:
    print("""Caso 1: Tienes obesidad o sobrepeso y la presión art. alta.\nDeberias considerar lo siguiente:\n 
          Médico, dieta sana, ejercicio, menos sal.""")
elif ps >= 129 and pd < 80:
    print("""Caso 2: Presión arterial elevada. Dirígete a un médico general.\nDeberias considerar lo siguiente:\n
           Mejor dieta, más actividad, menos estrés.""")
elif edad >= 40 and fumador == "si":
    print("""Caso 3: Edad mayor o igual a 40 años y fumador. Dirígete a un médico general.\nDeberias considerar lo siguiente:\n
          Dejar de fumar, chequeos médicos.""")
else:
    print("""Caso 4: Otros factores.
           Consulta médica, hábitos saludables.""")



