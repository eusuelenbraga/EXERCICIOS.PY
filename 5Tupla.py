#Quinto Exercício: Tupla de médias

def calcular_medias(dicionario_alunos):
    """
    Calcula a média de notas de cada aluno em um dicionário.

    Args:
      dicionario_alunos: Um dicionário onde as chaves são nomes de alunos e os valores são listas de notas.

    Returns:
      Uma lista de tuplas, onde cada tupla contém o nome do aluno e sua média de notas.
    """
    medias = []
    for aluno, notas in dicionario_alunos.items():
        media = sum(notas) / len(notas)
        medias.append((aluno, media))
    return medias

# Exemplo de uso
alunos = {
    "Suelen": [8.5, 9.0, 9.5],
    "Karynne": [7.0, 8.5, 10.0],
    "Samuca": [7.5, 10.0, 9.5]
}

medias_alunos = calcular_medias(alunos)
print(medias_alunos)