from collections import Counter

frase = input("Digite uma frase: ")

contador = Counter(frase)
mais_comuns = contador.most_common()

if len(mais_comuns) < 3:
    print("A frase possui menos de 3 caracteres únicos.")
else:
    terceiro = mais_comuns[2]
    
    freq_terceiro = terceiro[1]
    empatados = [char for char, freq in mais_comuns if freq == freq_terceiro]

    if len(empatados) > 1:
        print(
            f"Empate na 3ª posição. Caracteres: {', '.join(empatados)} (cada um aparece {freq_terceiro} vezes)"
        )
    else:
        print(f"3º caractere mais frequente: '{terceiro[0]}'")
        print(f"Quantidade: {terceiro[1]}")
