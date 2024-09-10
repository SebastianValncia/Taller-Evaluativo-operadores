tasa_cambio = float(input("Ingrese la tasa de cambio actual (1 USD = x COP): "))
def pesos_a_dolares(pesos):
    dolares = pesos / tasa_cambio
    return dolares


pesos = float(input(" Ingrese la cantidad de pesos a convertir: "))

dolares = pesos_a_dolares(pesos)
print(f"{pesos} pesos colombianos son equivalentes a {dolares:.2f} dólares")
