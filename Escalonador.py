class Escalonador:
    processos: list

    def __init__(self, processos: list):
        self.processos = processos
        self.processos.sort(key=lambda p: p.chegada)

    def executar_fcfs(self):
        wait_times = list()
        start_times = list()

        # First process doesn't wait
        wait_times.insert(0, 0)
        start_times.insert(0, self.processos[0].get_chegada())

        # But the others do
        for i in range(1, len(self.processos)):
            wait_time = self.processos[i - 1].get_duracao() - self.processos[i].get_chegada()
            wait_times.insert(i, wait_time)
            start_time = self.processos[i - 1].get_duracao()
            start_times.insert(i, start_time)

        duracao_total = 0
        for processo in self.processos:
            duracao_total += processo.get_duracao()

        instante_atual = 0
        ultimo_processo = 0
        output = self.__get_formatted_result_header__("First Come First Serve")
        while instante_atual <= duracao_total:
            for i in range(0, len(self.processos)):
                processo = self.processos[i]
                # Verificar se algum processo chegou neste instante
                if processo.chegada == instante_atual:
                    output += self.__get_formatted_result__(instante_atual, processo.pid, "Chegada")
                    # print("P" + str(processo.pid) + " chegou no instante " + str(instante_atual))

                if i == 0 and instante_atual == processo.get_chegada():
                    output += self.__get_formatted_result__(instante_atual, processo.pid, "Execução")
                    # print("P" + str(processo.pid) + " executou no instante " + str(instante_atual))

                # Verificar se algum processo terminou neste instante
                if instante_atual == start_times[i] + processo.duracao:
                    output += self.__get_formatted_result__(instante_atual, processo.pid, "Exit")
                    # print("P" + str(processo.pid) + " terminou no instante " + str(instante_atual))

                    # Verificar se outro processo pode iniciar no próximo instante
                    if ultimo_processo == len(self.processos) - 1:
                        break
                    else:
                        ultimo_processo += 1
                    proximo_processo = self.processos[ultimo_processo].get_id()
                    output += self.__get_formatted_result__(instante_atual, proximo_processo, "Execução")
                    # print("P" + str(proximo_processo) + " executou no instante " + str(instante_atual))
            instante_atual += 1
        return output

    # Shortest Job First
    def executar_sjf(self):
        remaining_times = self.__get_remaining_times__()
        wait_times = list()
        terminos = list()

        duracao_total = 0
        for processo in self.processos:
            duracao_total += processo.get_duracao()

        # First process doesn't wait
        first_duracao = self.processos[0].get_duracao()
        self.processos[0].set_duracao(0)
        sorted_list = sorted(self.processos, key=lambda p: p.get_duracao())

        wait_times.insert(0, 0)
        terminos.insert(0, sorted_list[0].get_chegada() + first_duracao)

        # But the others do
        for i in range(1, len(sorted_list)):
            wait_time = terminos[i - 1] - sorted_list[i].get_chegada()
            wait_times.insert(i, wait_time)
            termino = sorted_list[i].get_chegada() + wait_time + sorted_list[i].get_duracao()
            terminos.insert(i, termino)

        instante_atual = 0
        ultimo_processo = 0
        output = self.__get_formatted_result_header__("Shortest Job First")
        while instante_atual <= duracao_total:
            for i in range(0, len(self.processos)):
                processo = sorted_list[i]
                # Verificar se algum processo chegou neste instante
                if processo.chegada == instante_atual:
                    output += self.__get_formatted_result__(instante_atual, processo.pid, "Chegada")

                if i == 0 and instante_atual == processo.get_chegada():
                    output += self.__get_formatted_result__(instante_atual, processo.pid, "Execução")

                # Verificar se algum processo terminou neste instante
                if instante_atual == terminos[i]:
                    output += self.__get_formatted_result__(instante_atual, processo.pid, "Exit")
                    remaining_times[i] = 0

                    # Verificar se outro processo pode iniciar no próximo instante
                    if ultimo_processo == len(sorted_list) - 1:
                        break
                    else:
                        ultimo_processo += 1
                    proximo_processo = sorted_list[ultimo_processo].get_id()
                    if not self.__any_process_left__(remaining_times):
                        break
                    output += self.__get_formatted_result__(instante_atual, proximo_processo, "Execução")
            instante_atual += 1
        return output

    def __any_process_left__(self, remaining_times: list):
        for time in remaining_times:
            if time != 0:
                return True
        return False

    # Shortest Remaining Time
    def executar_srt(self):
        return

    # Round Robin
    ## TODO: Make this work
    def executar_rr(self, quantum: int):
        indice_processo_em_execucao = 0  # Começar pelo primeiro processo que chegou
        remaining_times = self.__get_remaining_times__()
        wait_times = self.__get_wait_times__()
        instante_atual = 0  # Representa o tempo
        fila_processos = list()
        quantum_atual = 0
        while True:
            # Cada iteração deste ciclo é 1 segundo
            # Receber os processos que chegaram neste instante
            for processo in self.processos:
                if processo.chegada == instante_atual:
                    print("P" + str(processo.pid) + " chegou no instante " + str(instante_atual))
                    fila_processos.append(processo.pid)

            # Se o processo terminou, removemos ele da fila
            if remaining_times[indice_processo_em_execucao] == 0:
                fila_processos.remove(fila_processos[indice_processo_em_execucao])
            else:
                remaining_times[indice_processo_em_execucao] -= 1  # Este processo executou durante 1 segundo
            print("Instante " + str(instante_atual + 1) + "=")
            print(remaining_times)

            if quantum_atual == quantum or remaining_times[indice_processo_em_execucao] == 0:
                # O quantum deste processo chegou ao fim, vamos ao próximo
                if indice_processo_em_execucao == len(fila_processos) - 1:
                    indice_processo_em_execucao = 0
                else:
                    indice_processo_em_execucao += 1
                quantum_atual = 0  # Resetar o quantum
                print("P" + str(fila_processos[indice_processo_em_execucao]) + " começou")

            quantum_atual += 1
            instante_atual += 1
            # Para o ciclo quando todos processos forem executados
            if not self.__existem_processos_em_espera__(remaining_times):
                print("Acabaram processos")
                break
        return

    # Funções Auxiliares
    def __get_remaining_times__(self):
        duracoes = list()
        for processo in self.processos:
            duracoes.append(processo.duracao)
        return duracoes

    def __get_wait_times__(self):
        wait_times = list()
        for _ in self.processos:
            wait_times.append(0)
        return wait_times

    def __existem_processos_em_espera__(self, remaining_times: list):
        for time in remaining_times:
            if time != 0:
                return True
        return False

    def __get_formatted_result_header__(self, algorithm_name: str):
        return "Algoritmo de escalonamento:" + algorithm_name + "\n" \
                 + "=============================================================\n" \
                 + "| Simulation Time\t| ID do Processo\t|\tEvento\t\t|\n"

    def __get_formatted_result__(self, instante: int, pid: int, evento: str):
        return "|\t\t" + str(instante) + "\t\t\t|\t\t" + str(pid) + "\t\t\t|\t" + evento + "\t\t|\n"
