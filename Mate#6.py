def generar_numeros_pseudoaleatorios(m, a, c, x0, n):
    if m <= 0 or a <= 0 or c < 0 or n <= 0 or x0 < 0 or x0 >= m:
        raise ValueError("Los valores de m, a, c, x0 y n deben cumplir las restricciones.")
    
    # Lista para almacenar los números pseudoaleatorios
    numeros = []
    
    # Generación de la secuencia
    x = x0
    for _ in range(n):
        x = (a * x + c) % m
        numeros.append(x)
    
    return numeros

# Ejemplo de uso con valores de prueba
try:
    m = int(input("Ingrese el valor de m: "))
    a = int(input("Ingrese el valor de a: "))
    c = int(input("Ingrese el valor de c: "))
    x0 = int(input("Ingrese el valor de la semilla x0: "))
    n = int(input("Ingrese la cantidad de números a generar: "))
    
    numeros = generar_numeros_pseudoaleatorios(m, a, c, x0, n)
    print("Números pseudoaleatorios generados:", numeros)
except ValueError as e:
    print("Error:", e)