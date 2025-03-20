#Segundo Exercício: Ordenação de Tuplas

def ordenar_por_idade(lista_pessoas):
  return sorted(lista_pessoas, key=lambda pessoa: pessoa[1])

pessoas = [("Suelen", 34), ("Samuel", 20), ("Karynne", 35), ("João", 23)]
pessoas_ordenadas = ordenar_por_idade(pessoas)
print(pessoas_ordenadas)