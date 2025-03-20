#Sexto Exercício: Combinação de dicionários

def combinar_dicionarios(dicionario1, dicionario2):
    resultado = dicionario1.copy()  

    for chave, valor in dicionario2.items():
        if chave in resultado:
            resultado[chave] += valor 
        else:
            resultado[chave] = valor  

    return resultado

dicionario1 = {"a": 1, "b": 2, "c": 3}
dicionario2 = {"b": 3, "c": 4, "d": 5}

dicionario_combinado = combinar_dicionarios(dicionario1, dicionario2)
print(dicionario_combinado)