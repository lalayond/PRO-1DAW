def run(data: dict, target_keys: tuple) -> dict:
    # Usamos comprensión de diccionarios para crear un nuevo diccionario (pdata).
    # Recorremos cada clave en 'target_keys' y solo agregamos las que existen en 'data'.
    pdata = {key: data[key] for key in target_keys if key in data}

    # Devolvemos el nuevo diccionario (pdata) que solo tiene las claves presentes en 'target_keys' y en 'data'.
    return pdata


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor
