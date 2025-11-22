produtos = {
    "Alimentação": [12.50, 8.99, 15.30],
    "Limpeza": [5.20, 7.80],
    "Higiene": [10.00, 12.00, 9.50, 14.00],
}

medias = {
    categoria: sum(valores) / len(valores) for categoria, valores in produtos.items()
}
categoria_vencedora = max(medias, key=medias.get)

print(f"Categoria vencedora: {categoria_vencedora}")
print(f"Média: {medias[categoria_vencedora]:.2f}")
