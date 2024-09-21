from random import randint
from settings import *


def tratarNomeLoot(nome, qtde):
    palavra1 = nome.split()[0]
    if palavra1 == "Pacote" or palavra1 == "Conjunto" or palavra1 == "Caixa":
        return f"{nome} contendo ({qtde}) unidades."
    return f"({qtde}) {nome}"


class Loot:

    def __init__(self, cursor):
        self.cursor = cursor

    def contarLinhas(self):
        return self.cursor.execute("SELECT COUNT(*) FROM drop_zumbis").fetchone()[0]

    def gerarLootZumbi(self):
        id = gerarIdAleatorio(self.contarLinhas())
        nome, qtdeMax = self.cursor.execute(f"SELECT Nome, qtdeMax FROM drop_zumbis WHERE id={id}").fetchone()
        qtde = randint(1, qtdeMax)
        return tratarNomeLoot(nome, qtde)