from datetime import datetime
from Escalonador import Escalonador
from Programa import Programa
from Processo import Processo


def __get_formatted_process_list__(processos: list):
    output = "| ID Processo\t| Tempo de chegada\t| Duração\t|\n"
    for processo in processos:
        output += "|\t\t" + str(processo.pid) + \
                  "\t\t|\t\t\t" + str(processo.chegada) + \
                  "\t\t|\t\t" + str(processo.duracao) + "\t|\n"
    return output


def __write_file__(content: str):
    today = datetime.now()
    formatted_date = today.strftime("%Y%m%d_%H%M")
    filename = "resultado_" + formatted_date + ".log"
    new_file = open(filename, "w")
    new_file.write(content)
    new_file.close()
    return filename


def __imprimir_resultado__(resultado: str):
    print(resultado)
    filename = __write_file__(resultado)
    print("Dados guardados em " + filename)


def pedir_opcao():
    opcao = int(input("Escolha a opção:"))
    if opcao > 5 or opcao < 1:
        print("Opção Inválida!")
        return pedir_opcao()
    return opcao


def pedir_quantum():
    quantum = int(input("Qual é o quantum a usar?"))
    if quantum < 1:
        print("O quantum tem de ser positivo e maior do que 0!")
        return pedir_quantum()
    return quantum


def mostrar_menu():
    print("=======MENU======")
    print("1. Executar FCFS")
    print("2. Executar SRT")
    print("3. Executar SJF")
    print("4. Executar RR")
    print("5. Sair")
    opcao = pedir_opcao()
    # processos = Programa().gerar_lista_processos(3)
    processos = [
        Processo().set_chegada_duracao(0, 12),
        Processo().set_chegada_duracao(3, 6),
        Processo().set_chegada_duracao(5, 2),
        Processo().set_chegada_duracao(8, 5),
        Processo().set_chegada_duracao(13, 8)
    ]

    # processos = [
    #     Processo().set_chegada_duracao(0, 1),
    #     Processo().set_chegada_duracao(0, 1),
    #     Processo().set_chegada_duracao(0, 1),
    #     Processo().set_chegada_duracao(3, 1),
    #     Processo().set_chegada_duracao(3, 2),
    #     Processo().set_chegada_duracao(3, 3),
    #     Processo().set_chegada_duracao(7, 3),
    #     Processo().set_chegada_duracao(7, 2),
    #     Processo().set_chegada_duracao(7, 1),
    #     Processo().set_chegada_duracao(13, 1),
    #     Processo().set_chegada_duracao(13, 2),
    #     Processo().set_chegada_duracao(13, 3),
    #     Processo().set_chegada_duracao(17, 1),
    #     Processo().set_chegada_duracao(17, 2)
    # ]

    # processos = [
    #     Processo().set_chegada_duracao(3, 9),
    #     Processo().set_chegada_duracao(6, 4),
    #     Processo().set_chegada_duracao(9, 12),
    #     Processo().set_chegada_duracao(12, 3)
    # ]
    escalonador = Escalonador(processos)
    if opcao == 1:
        resultado = escalonador.executar_fcfs()
        __imprimir_resultado__(__get_formatted_process_list__(processos) + "\n" + resultado)
    elif opcao == 2:
        resultado = escalonador.executar_srt()
        __imprimir_resultado__(__get_formatted_process_list__(processos) + "\n" + resultado)
    elif opcao == 3:
        resultado = escalonador.executar_sjf()
        __imprimir_resultado__(__get_formatted_process_list__(processos) + "\n" + resultado)
    elif opcao == 4:
        quantum = pedir_quantum()
        resultado = escalonador.executar_rr(quantum)
        __imprimir_resultado__(__get_formatted_process_list__(processos) + "\n" + resultado)
    else:
        print("Até a próxima!")
        return
    mostrar_menu()


if __name__ == '__main__':
    mostrar_menu()
