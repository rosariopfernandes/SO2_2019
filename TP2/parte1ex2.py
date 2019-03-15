import os
from random import randint
from math import sqrt


# Calcula hipotenusas de números aleatórios


def calcular_hipotenusas():
    # Lista para armazenar os resultados
    hipotenusas = list()
    # Repete 9999999 vezes
    for i in range(0, 10000000 - 1):
        # Calcular a hipotenusa e guardar na lista
        hipotenusa = sqrt((randint(1, 1000) * randint(1, 1000)) + (randint(1, 1000) * randint(1, 1000)))
        hipotenusas.append(round(hipotenusa, 2))
    return hipotenusas


if __name__ == '__main__':
    print("pid = " + str(os.getpid()))
    print("A calcular hipotenusas...")
    hipotenusas = calcular_hipotenusas()
    # print(hipotenusas)
