from modulo import *

def menu():
    while True:  # Bucle infinito para mantener el menú activo
        print("\nSeleccione la ecuación que desea calcular:")
        print("1. Δx = v × Δt (Desplazamiento con velocidad constante)")
        print("2. Δx = Vi × Δt + (α × Δt^2) / 2 (Desplazamiento con aceleración)")
        print("3. Vf = Vi + α × Δt (Velocidad final con aceleración)")
        print("4. Salir")
        opcion = int(input("Ingrese la opción (1/2/3/4): "))

        if opcion == 1:
            v = float(input("Ingrese la velocidad (v) en m/s: "))
            t = float(input("Ingrese el tiempo (Δt): "))
            unidad = input("¿La unidad del tiempo es segundos (s) o milisegundos (ms)? ").lower()
            t = convertir_tiempo_a_segundos(t, unidad)
            resultado = calcular_desplazamiento_velocidad_constante(v, t)
            print(f"El desplazamiento (Δx) es: {resultado} metros")

        elif opcion == 2:
            Vi = float(input("Ingrese la velocidad inicial (Vi) en m/s: "))
            t = float(input("Ingrese el tiempo (Δt): "))
            a = float(input("Ingrese la aceleración (α) en m/s²: "))
            unidad = input("¿La unidad del tiempo es segundos (s) o milisegundos (ms)? ").lower()
            t = convertir_tiempo_a_segundos(t, unidad)
            resultado = calcular_desplazamiento_con_aceleracion(Vi, t, a)
            print(f"El desplazamiento (Δx) es: {resultado} metros")

        elif opcion == 3:
            Vi = float(input("Ingrese la velocidad inicial (Vi) en m/s: "))
            t = float(input("Ingrese el tiempo (Δt): "))
            a = float(input("Ingrese la aceleración (α) en m/s²: "))
            unidad = input("¿La unidad del tiempo es segundos (s) o milisegundos (ms)? ").lower()
            t = convertir_tiempo_a_segundos(t, unidad)
            resultado = calcular_velocidad_final(Vi, t, a)
            print(f"La velocidad final (Vf) es: {resultado} m/s")

        elif opcion == 4:
            print("Saliendo del programa.")
            break 

        else:
            print("Opción no válida, intente de nuevo.")

menu()