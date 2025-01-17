 # Diccionario para almacenar la cantidad de repeticiones de cada número
    frequency = {}
    target_num = -1  # Inicializar el valor predeterminado

    # Recorrer los números en la lista
    for number in numbers:
        # Incrementar el conteo del número en el diccionario
        if number in frequency:
            frequency[number] += 1
        else:
            frequency[number] = 1

        # Verificar si este número se ha repetido nrep veces
        if frequency[number] == nrep:
            target_num = number
            break  # Salir del bucle al encontrar el primer número que cumple la condición

    # Devolver el número encontrado o el valor predeterminado (-1)
    return target_num
