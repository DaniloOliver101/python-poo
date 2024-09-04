tempo = input("Digite o tempo:")
distancia = input("Informe a distância>:")
tempo = float(tempo)
distancia = float(distancia)


if (tempo == 0):
    print("O tempo não pode ser zero.")
else:
    velocidade = distancia / tempo
    print("Velocidade:", velocidade)
