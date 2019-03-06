from datetime import datetime
from Escalonador import Escalonador
from Programa import Programa


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


def pedir_tempo():
    tempo = int(input("Qual é o tempo total da simulação?"))
    if tempo < 1:
        print("O tempo tem de ser positivo e maior do que 0!")
        return pedir_tempo()
    return tempo


def mostrar_menu():
    tempo_total = pedir_tempo()
    processos = Programa().gerar_lista_processos(tempo_total)
    escalonador = Escalonador(processos, tempo_total)
    print("=======MENU======")
    print("1. Executar FCFS")
    print("2. Executar SRT")
    print("3. Executar SJF")
    print("4. Executar RR")
    print("5. Sair")
    opcao = pedir_opcao()
    resultado = __get_formatted_process_list__(processos) + "\n"
    if opcao == 1:
        resultado += escalonador.executar_fcfs()
    elif opcao == 2:
        # resultado += escalonador.executar_srt()
        resultado += "Ainda não foi implementado SRT"
    elif opcao == 3:
        resultado += escalonador.executar_sjf()
    elif opcao == 4:
        # quantum = pedir_quantum()
        # resultado += escalonador.executar_rr(quantum)
        resultado += "Ainda não foi implementado RR"
    else:
        print("Até a próxima!")
        return
    __imprimir_resultado__(resultado)
    mostrar_menu()


if __name__ == '__main__':
    mostrar_menu()
