def calcular_salario_e_rendimentos():
    SC = float(input("Digite o salário de Clara: "))

    if SC <= 0:
        print("O salário deve ser maior que zero.")
        return

    SF = SC / 3

    print(f"O salário de Flora é: R$ {SF:.2f}")
    print(f"O salário de Clara é: R$ {SC:.2f}")

    RF = SF
    RC = SC
    mes = 0

    while RF < RC:
        RF += RF * 0.005
        RC += RC * 0.002
        mes += 1

    print(f"Após {mes} meses, Flora tem um valor igual ou maior que Clara.")
    print(f"Valor acumulado de Flora: R$ {RF:.2f}")
    print(f"Valor acumulado de Clara: R$ {RC:.2f}")


def main():
    calcular_salario_e_rendimentos()


if __name__ == "__main__":
    main()