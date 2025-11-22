valor = input("Digite um número: ")

try:
    numero = float(valor)
    if numero.is_integer():
        inteiro = int(numero)
        if inteiro % 2 == 0:
            print(f"O número {inteiro} é inteiro e par.")
        else:
            print(f"O número {inteiro} é inteiro e ímpar.")
    else:
        parte_inteira = int(numero)
        parte_decimal = abs(numero - parte_inteira)
        print(f"O número é decimal.")
        print(f"Parte inteira: {parte_inteira}")
        print(f"Parte decimal: {parte_decimal:.2f}")
except ValueError:
    print("Erro: O valor digitado não pode ser convertido para número.")
