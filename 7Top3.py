#Sétimo Exercício: Top 3 mais frequentes

from collections import Counter

def top_3_mais_frequentes(lista_numeros):
    contagem = Counter(lista_numeros)  
    ordenado = sorted(contagem.items(), key=lambda item: (-item[1], item[0]))  
    return [numero for numero, frequencia in ordenado[:3]]  

numeros = [40,40,10,40,10,40,40,30,40,40]
resultado = top_3_mais_frequentes(numeros)
print(resultado)