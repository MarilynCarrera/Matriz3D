#Diccionario
informacion_personal = {
    "nombre": "Dayana",
    "edad": 24,
    "ciudad": "El Chaco",
    "profesion": "Ingeniera"
}

# Valor asociado con la clave "ciudad"
informacion_personal["ciudad"] = "Loja"

#Nueva clave-valor representa la "profesion" de la persona
informacion_personal["profesion"] = "Desarrolladora de Software"

#Clave "telefono", número de teléfono
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "123-456-7890"

# Eliminar clave "edad" del diccionario
informacion_personal.pop("edad")

# Imprimir el diccionario actualizado
print(informacion_personal)
