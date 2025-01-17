# Lista para almacenar los registros con IDs corregidos
    fixed_db = []

    # Reasignar los IDs secuenciales a cada registro
    for idx, entry in enumerate(db):
        # Asignar el nuevo ID secuencial
        entry['id'] = idx + 1
        # Añadir el registro con ID corregido a la lista
        fixed_db.append(entry)

    # Devolver la base de datos con los IDs corregidos
    return fixed_db
