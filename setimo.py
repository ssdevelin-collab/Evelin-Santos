livros = [
    {"titulo": "A", "ano": 2020, "preco": 45},
    {"titulo": "B", "ano": 2024, "preco": 80},
    {"titulo": "C", "ano": 2020, "preco": 50},
    {"titulo": "D", "ano": 2022, "preco": 40},
]


agrupados = {}
for livro in livros:
    ano = livro["ano"]
    if ano not in agrupados:
        agrupados[ano] = []
    agrupados[ano].append(livro)


anos_ordenados = sorted(agrupados.keys())


for ano in anos_ordenados:
    livros_ano = agrupados[ano]
    media_preco = sum(l["preco"] for l in livros_ano) / len(livros_ano)
    print(f"\nAno: {ano} (Preço médio: {media_preco:.2f})")
    for livro in livros_ano:
        print(f" - {livro['titulo']} (R$ {livro['preco']:.2f})")
