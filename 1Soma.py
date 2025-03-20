#Primeiro Exercício: Soma de elementos pares

def somar_pares(lista_numeros):
    soma = 0
    for numero in lista_numeros:
        if numero % 2 == 0:
            soma += numero
    return soma

numeros = [1, 2, 3, 4, 5]
resultado = somar_pares(numeros)
print(f"A soma dos números pares é {resultado}")