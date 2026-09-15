def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32
def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9
def dolar_to_bolivar(dolar):
    """Convert Dolar to Bolivar."""
    return dolar * 800.00
def bolivar_to_dolar(bolivar):
    """Convert Bolivar to Dolar."""
    return bolivar / 800.00

# multiconversor modular de grados y bolivares #

def menu():
    """Ejecuta una interfaz de consola interactiva para el usuario."""
    while True:
        print("\n=== CONVERTIDOR MULTIFUNCIONAL ===")
        print("1. Celsius a Fahrenheit")
        print("2. Fahrenheit a Celsius")
        print("3. Dólares (USD) a Bolívares (VES)")
        print("4. Bolívares (VES) a Dólares (USD)")
        print("5. Salir")
        
        opcion = input("Selecciona una opción (1-5): ")
        
        if opcion == "5":
            print("¡Hasta luego!")
            break
            
        if opcion in ["1", "2", "3", "4"]:
            try:
                valor = float(input("Introduce el valor a transformar: "))
                
                if opcion == "1":
                    print(f"Resultado: {valor}°C equivalen a {celsius_to_fahrenheit(valor):.2f}°F")
                elif opcion == "2":
                    print(f"Resultado: {valor}°F equivalen a {fahrenheit_to_celsius(valor):.2f}°C")
                elif opcion == "3":
                    print(f"Resultado: ${valor:.2f} USD equivalen a {dolar_to_bolivar(valor):.2f} VES")
                elif opcion == "4":
                    print(f"Resultado: {valor:.2f} VES equivalen a ${bolivar_to_dolar(valor):.2f} USD")
            except ValueError:
                print("Error: Por favor, introduce un número válido.")
        else:
            print("Opción no válida. Intenta de nuevo.")

# Punto de entrada para ejecutar el programa
if __name__ == "__main__":
    menu()
