# Crear_archivo_my_notes.txt
with open("my_notes.txt", "w") as file:
    file.write("1. Recordar comprar huevos en el supermercado.\n")
    file.write("2. Investigar nuevas recetas de postres.\n")
    file.write("3. Llamar al doctor para programar cita.\n")

# Abrir_leer_el_archivo
with open("my_notes.txt", "r") as file:
    # Leer el contenido línea por línea
    lines = file.readlines()

    # Mostrar_cada_línea_en_la_consola
    for line in lines:
        print(line.strip())  # strip() elimina cualquier espacio en blanco adicional, como saltos de línea

# Cerrar_archivo
file.close()
