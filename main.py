from dataclasses import dataclass

@dataclass
class Numero:
    valor: int

    def analizar(self):
        if self.valor % 2 == 0:
            print("El número es par.")
            if self.valor == 10:
                print("Este número es especial porque es 10.")
        else:
            print("El número es impar.")
            if self.valor == 7:
                print("¡Has ingresado el número mágico: 7!")

    def dividir(self, otro_valor):
        resultado = self.valor / otro_valor
        print(f"La divison entre {self.valor} y {otro_valor} es: {resultado}")

# Ejecución del programa
if __name__ == "__main__":
    try:
        entrada = int(input("Introduce un número: "))
        num = Numero(entrada)
        num.analizar()
        num.dividir(2)  # Cambia este número si quieres sumar otro valor
    except ValueError:
        print("Por favor, ingresa un número válido.")
        print("Nueva Linea")