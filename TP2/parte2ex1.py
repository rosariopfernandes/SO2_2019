from math import sqrt
from sys import maxsize
import msvcrt


# Verifica se um número é primo
def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(sqrt(n)) + 1, 2))


def main():
    n_vezes = 0
    ultimo_primo = 0
    soma = 0
    for i in range(1, maxsize):
        if not is_prime(i):
            continue
        pressed_key = msvcrt.getch()
        if pressed_key == 'c':
            break
        n_vezes += 1
        ultimo_primo = i
        soma += i
    print("Número de vezes: " + str(n_vezes))
    print("Último Primo: " + str(ultimo_primo))
    print("Soma: " + str(soma))


if __name__ == '__main__':
    main()
