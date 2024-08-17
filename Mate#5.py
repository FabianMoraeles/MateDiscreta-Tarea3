def hash_dispersión(tamaño, lista_numeros):
    if not isinstance(tamaño, int) or tamaño <= 0:
        raise ValueError("El tamaño debe ser un entero positivo.")
    
    memoria_hash = [-1] * tamaño
    
    for num in lista_numeros:
        if not isinstance(num, int) or num < 0:
            raise ValueError("Los números a almacenar deben ser enteros no negativos.")
        
        pos = num % tamaño
        
        while memoria_hash[pos] != -1:
            pos = (pos + 1) % tamaño
        
        memoria_hash[pos] = num
    
    return memoria_hash

try:
    tamaño = int(input("Ingrese la cantidad de celdas de memoria: "))
    lista_numeros = list(map(int, input("Ingrese los números a almacenar separados por espacios: ").split()))
    
    resultado = hash_dispersión(tamaño, lista_numeros)
    print("Memoria después del hashing:", resultado)
except ValueError as e:
    print("Error:", e)