import os
from random import randint


# Gera um número aleatório de 1 a 10000
# Pede ao utilizador para advinhar qual é.


def input_guess(generated_number: int):
    while True:
        # Pedir ao utilizador para advinhar o número:
        tentativa = int(input("Advinhe qual é número:"))
        if tentativa == generated_number:
            # O utilizador acertou.
            break
        else:
            # O utilizador errou.
            # Informamos se o número é maior ou menor
            # do que a última tentativa.
            if tentativa > generated_number:
                print("Muito alto. Tente um número menor")
            else:
                print("Muito baixo. Tente um número maior")


def io_bound():
    # Imprimir o uid do utilizador
    print("uid = " + str(os.getuid()))
    # Gerar um número aleatório de 1 a 10000:
    random_number = randint(1, 10000)
    print("Foi gerado um número entre 1 à 10000.")
    # Pedir ao utilizador para advinhar o número
    # até que ele acerte.
    input_guess(random_number)
    print("Parabéns! Você acertou, o número era " + str(random_number))


if __name__ == '__main__':
    io_bound()
