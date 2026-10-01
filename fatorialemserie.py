def fatorial(num):
    resultado = 1

    for i in range(1, num + 1):
        resultado = resultado * i

    return resultado


def divisao(num1, num2):
    resultado = num1 / num2

    return resultado


def main():
    n = int(input("Digite o valor de N: "))

    soma = 1

    for i in range(1, n + 1):
        fat = fatorial(i)
        resultado = divisao(1, fat)

        soma = soma + resultado

    print("Resultado:", soma)


main()