def calcular_desplazamiento_velocidad_constante(velocidad, tiempo):
    # Δx = v × Δt
    desplazamiento = velocidad * tiempo
    print(f"Operación: Δx = {velocidad} × {tiempo} = {desplazamiento}")
    return desplazamiento

def calcular_desplazamiento_con_aceleracion(velocidad_inicial, tiempo, aceleracion):
    # Δx = Vi × Δt + (α × Δt^2) / 2
    desplazamiento = velocidad_inicial * tiempo + (aceleracion * tiempo**2) / 2
    print(f"Operación: Δx = {velocidad_inicial} × {tiempo} + ({aceleracion} × {tiempo}^2) / 2 = {desplazamiento}")
    return desplazamiento

def calcular_velocidad_final(velocidad_inicial, tiempo, aceleracion):
    # Vf = Vi + α × Δt
    velocidad_final = velocidad_inicial + aceleracion * tiempo
    print(f"Operación: Vf = {velocidad_inicial} + {aceleracion} × {tiempo} = {velocidad_final}")
    return velocidad_final

def convertir_tiempo_a_segundos(tiempo, unidad):
    if unidad == 'ms':
        return tiempo / 1000 
    elif unidad == 's':
        return tiempo 
    else:
        print("Unidad no reconocida, asumiendo segundos.")
        return tiempo