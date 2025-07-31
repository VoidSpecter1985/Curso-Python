def pedir_calificaciones():
    calificaciones = []
    cantidad = int(input("¿Cuántas calificaciones vas a ingresar? "))

    for i in range(cantidad):
        nota = float(input(f"Ingrese la calificación #{i + 1}: "))
        while nota < 0 or nota > 10:
            print("Calificación inválida. Debe estar entre 0 y 10.")
            nota = float(input(f"Reingrese la calificación #{i + 1}: "))
        calificaciones.append(nota)

    return calificaciones

def calcular_promedio(calificaciones):
    return sum(calificaciones) / len(calificaciones)

def mostrar_resultado(promedio):
    print(f"\nPromedio final: {promedio:.2f}")
    if promedio >= 3.0:
        print("¡Aprobaste!")
    else:
        print("No aprobaste. ¡Sigue intentándolo!")

def main():
    print("=== Calculadora de Promedio ===")
    calificaciones = pedir_calificaciones()
    promedio = calcular_promedio(calificaciones)
    mostrar_resultado(promedio)
if __name__ == "__main__":
    main()