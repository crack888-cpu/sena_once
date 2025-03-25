compra_total = int(input("Ingrese el valor total de la compra: "))
pago = int(input("Ingrese su forma de pago:\n1. Efectivo\n2. Tarjeta de credito\n"))
if compra_total > 100 and pago == 1:
    desc = compra_total - ((compra_total - compra_total * 0.1)*0.05) 
    print("El valor a pagar es: ", desc)
elif compra_total > 100 and pago == 2:
    desc = compra_total - compra_total * 0.1
    print("El valor a pagar es: ", desc)
elif compra_total < 100 and pago == 1:
    desc = compra_total - compra_total * 0.05
    print("El valor a pagar es: ", desc)
elif compra_total < 100 and pago == 2:
    print("El valor a pagar es: ", compra_total)