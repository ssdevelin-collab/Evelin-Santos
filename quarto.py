def produto_escalar(vetor1, vetor2):
    if len(vetor1) != len(vetor2):
        raise ValueError("Os vetores devem ter o mesmo tamanho.")
    return sum(v1 * v2 for v1, v2 in zip(vetor1, vetor2))


n = int(input("Digite o tamanho dos vetores: "))
vetor1 = [float(input(f"Elemento {i+1} do primeiro vetor: ")) for i in range(n)]
vetor2 = [float(input(f"Elemento {i+1} do segundo vetor: ")) for i in range(n)]

resultado = produto_escalar(vetor1, vetor2)
print(f"\nProduto escalar: {resultado}")
