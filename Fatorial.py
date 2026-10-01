def fatorial(num):
    resultado = 1

    for i in range(1, num + 1):
        resultado = resultado * i

    return resultado


def main():
    num = int(input("Digite um número: "))

    resultado = fatorial(num)

    print("Fatorial:", resultado)


main()

if __name__ == "__main__":
    main()