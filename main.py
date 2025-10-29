#Un número perfecto es un número entero positivo que es igual a la suma de sus divisores.
def is_perfect(n):
    if n <= 0:
        raise ValueError("El número debe ser positivo")
    
    suma = sum(i for i in range(1, n) if n % i == 0)
    return suma == n

