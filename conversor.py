def usd_ves(tasa_bcv, usd):
    total = usd * tasa_bcv
    return round(total, 2)

def ves_usd(tasa_bcv, ves):
    if tasa_bcv == 0:
        return 0
    total = ves / tasa_bcv
    return round(total, 2)

print("Calculadora de divisas")

while True:
    print("que quieres hacer?")
    print("1. Convertir usd a ves")
    print("2. Convertir ves a usd")
    print("3. Salir")

    opcion = input("Elige una opcion (1, 2, 3): ")

    if opcion == "3":
        print("saliendo... ")
        break

    tasa = float(input("Ingrese la tasa del día: "))

    if opcion == "1":
        monto_usd = float(input("Cuántos dólares desea cambiar?"))
        resultado = usd_ves(tasa, monto_usd)
        print(f"{monto_usd} USD equivalen a {resultado} VES")

    elif opcion == "2":
        if tasa == 0:
            print("Error, no puede ser igual a 0")
        else:
            monto_ves = float(input("cuántos bolivares desea cambiar?: "))
            resultado = ves_usd(tasa, monto_ves)
            print(f"{monto_ves} ves equivalen a {resultado}$ ")