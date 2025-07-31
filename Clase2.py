# PROGRAMA PARA VERIFICAR UN NÚMERO INGRESADO

def verificar(valor):
    # Comprobación de casos especiales
    if valor == 20:
        print("Has ingresado el número veinte")
    elif valor == 10:
        print("¡El número diez es un comodín!")
    elif valor % 2 == 0:
        print("El número ingresado es par")
    else:
        print("El número ingresado es impar")

def main():
    print("=== Bienvenido al verificador de números ===")
    try:
        numero_usuario = int(input("Escribe un número para analizar: "))
        verificar(numero_usuario)
    except ValueError:
        print("Error: Solo se permiten números enteros válidos.")

if __name__ == "__main__":
    main()