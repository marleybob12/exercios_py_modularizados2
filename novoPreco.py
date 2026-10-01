def calcularNovoPreco(preco, vendaMensal):
    if vendaMensal < 500 and preco < 30:
        novoPreco = preco * 1.10

    elif vendaMensal >= 500 and vendaMensal < 1000 and preco >= 30 and preco < 80:
        novoPreco = preco * 1.15

    elif vendaMensal >= 1000 and preco >= 80:
        novoPreco = preco * 0.95

    else:
        novoPreco = preco

    print("Novo preço: R$", novoPreco)


def main():
    preco = float(input("Digite o preço atual do produto: "))
    vendaMensal = int(input("Digite a média mensal de vendas: "))

    calcularNovoPreco(preco, vendaMensal)


main()

if __name__ == "__main__":
    main()