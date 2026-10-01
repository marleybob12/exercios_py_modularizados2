def calcularVelocidade(voltas, extensao, tempo):
    distanciaMetros = voltas * extensao
    distanciaKm = distanciaMetros / 1000
    tempoHoras = tempo / 60

    velocidadeMedia = distanciaKm / tempoHoras

    print("Velocidade média:", velocidadeMedia, "km/h")


def main():
    voltas = int(input("Digite o número de voltas: "))
    extensao = float(input("Digite a extensão do circuito em metros: "))
    tempo = float(input("Digite o tempo da corrida em minutos: "))

    calcularVelocidade(voltas, extensao, tempo)


main()


if __name__ == "__main__":
    main()
    