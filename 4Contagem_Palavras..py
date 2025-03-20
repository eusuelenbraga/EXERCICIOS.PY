#Quarto Exercício: Contagem de Palavras

import string

def contar_palavras(texto):
  
    texto = texto.translate(str.maketrans('', '', string.punctuation)).lower()

    palavras = texto.split() 
    contagem = {}

    for palavra in palavras:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1

    return contagem

texto = "Verificar se tem alguma palavra repetida. Analisar se tem alguma palavra repetida. Verificar se alguma palavra esta repetida"
resultado = contar_palavras(texto)
print(resultado)