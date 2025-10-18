from random import choice, randint


def apresentacao():
        return ', prazer! Sou um bot simples!'


def gerarIdAleatorio(qtdeMax):
    return randint(1, qtdeMax)


def printarAmarelo(texto):
    print(f"\033[93m {texto}\033[00m")
