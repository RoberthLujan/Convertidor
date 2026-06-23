def aplicar_bonificacion_por_referencia(lista_precios, porcentaje):
    print(f"\nDirección de memoria recibida: {id(lista_precios)}")
    
    for i in range(len(lista_precios)):
        lista_precios[i] = round(lista_precios[i] * (1 + porcentaje / 100), 2)
        
    print(f"¡Lista modificada internamente!")

#PROGRAMA PRINCIPAL 

print("SIMULADOR DE PASO POR REFERENCIA INTERACTIVO")

n = int(input("¿Cuántos productos deseas registrar?: "))
precios_originales = []

for i in range(n):
    precio = float(input(f"Ingrese el precio del producto {i+1}:"))
    precios_originales.append(precio)

print("\nEstado Inicial")
print(f"1. Lista original: {precios_originales}")
print(f"2. Dirección de memoria original: {id(precios_originales)}")


porcentaje_aumento = float(input("\n¿Qué porcentaje de aumento deseas aplicar? (Ej: 10 para 10%): "))

print("\nLlamando a la función")

aplicar_bonificacion_por_referencia(precios_originales, porcentaje_aumento)

print("\nDe regreso en el programa principal")

print(f"3. Lista final (afectada por el efecto colateral): {precios_originales}")
print(f"4. Dirección de memoria final: {id(precios_originales)}")