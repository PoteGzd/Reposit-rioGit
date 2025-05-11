def soma_valores(numeros):
    soma = sum(numeros)
    return soma
def main():
    numeros = []
    print("Digite -1 para finalizar")
    while True:
        numero = float(input("Digite o número para ser somado"))
        if numero == -1:
            break
        numeros.append(numero)
        soma = soma_valores(numeros)
    print(f"A soma dos valores é:{soma}")
main()