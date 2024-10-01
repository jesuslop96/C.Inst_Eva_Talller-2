#Suma de pares

def Suma (Numeros):
    suma = 0
    for num in Numeros:
        if num %2 == 0:
            suma += num
    return suma

Lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

Resultado = Suma(Lista)

print("La suma de los pares es de:",Resultado)