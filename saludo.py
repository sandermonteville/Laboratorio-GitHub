def saludar(nombre_completo):
    if nombre_completo is None or not nombre_completo.strip():
        return "Error: el nombre no puede estar vacío ni ser nulo"

    return f"Hola {nombre_completo}"

print(saludar("Diego Mendoza"))
