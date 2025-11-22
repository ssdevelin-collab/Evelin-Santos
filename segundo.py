quantidade = int(input("Digite a quantidade de pares (nome e nota): "))
pares = []

for i in range(quantidade):
    nome = input(f"Digite o nome do aluno {i+1}: ")
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    pares.append((nome, nota))

dicionario = {}
for nome, nota in pares:
    if nome in dicionario:
        dicionario[nome].append(nota)
    else:
        dicionario[nome] = [nota]

medias = {nome: sum(notas) / len(notas) for nome, notas in dicionario.items()}
ordenado = sorted(medias.items(), key=lambda x: x[1])

print("\nAlunos em ordem crescente de média:")
for nome, media in ordenado:
    print(f"{nome}: {media:.2f}")
