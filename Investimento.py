def calcularInvestimento(tipo, valor):
    if tipo == 1:
        valorCorrigido = valor * 1.03
        print("Valor corrigido: R$", valorCorrigido)

    elif tipo == 2:
        valorCorrigido = valor * 1.05
        print("Valor corrigido: R$", valorCorrigido)

    else:
        print("Tipo de investimento inválido.")


def main():
    tipo = int(input("Digite o tipo de investimento (1 - Poupança / 2 - Renda Fixa): "))
    valor = float(input("Digite o valor do investimento: R$ "))

    calcularInvestimento(tipo, valor)


main()

if __name__ == "__main__":
    main()