class Escalonador:
    processos: list

    __tipos_evento__ = {
        0: "Chegada",
        1: "Execução",
        2: "Exit"
    }

    def __init__(self, processos: list):
        self.processos = processos
        self.processos.sort(key=lambda p: p.chegada)

    def executar_fcfs(self):
        wait_times = list()
        start_times = list()
        terminos = list()
        duracao_total = 0
        eventos = dict()

        for processo in self.processos:
            duracao_total += processo.get_duracao()
            # Adicionar as chegadas
            eventos[processo.get_chegada()] = list()
            eventos[processo.get_chegada()].append(str(self.__get_formatted_result__(processo.get_chegada(),
                                                                                     processo.pid, "Chegada")))

        # First process doesn't wait
        wait_times.insert(0, 0)
        start_times.insert(0, self.processos[0].get_chegada())
        termino = self.processos[0].get_chegada() + self.processos[0].get_duracao()
        terminos.insert(0, termino)
        self.__add_event__(self.processos[0].get_chegada(), self.processos[0].get_id(), 1, eventos)
        self.__add_event__(termino, self.processos[0].get_id(), 2, eventos)

        # But the others do
        for i in range(1, len(self.processos)):
            wait_time = self.processos[i - 1].get_duracao() - self.processos[i].get_chegada()
            wait_times.insert(i, wait_time)

            start_time = start_times[i - 1] + self.processos[i - 1].get_duracao()
            start_times.insert(i, start_time)
            self.__add_event__(start_time, self.processos[i].get_id(), 1, eventos)

            termino = start_time + self.processos[i].get_duracao()
            self.__add_event__(termino, self.processos[i].get_id(), 2, eventos)

        output = self.__get_formatted_result_header__("First Come First Serve")
        output += self.__print_events(eventos)

        throughput = len(self.processos) / duracao_total
        output += self.__get_statistics__(0, 0, throughput, 0)
        return output

    # Shortest Job First
    def executar_sjf(self):
        wait_times = list()
        terminos = list()
        duracao_total = 0
        eventos = dict()
        for processo in self.processos:
            duracao_total += processo.get_duracao()
            # Adicionar as chegadas
            eventos[processo.get_chegada()] = list()
            eventos[processo.get_chegada()].append(str(self.__get_formatted_result__(processo.get_chegada(),
                                                                                     processo.pid, "Chegada")))

        # First process doesn't wait
        first_duracao = self.processos[0].get_duracao()
        sorted_list = list(self.processos)
        sorted_list[0].set_duracao(0)
        sorted_list.sort(key=lambda p: p.get_duracao())
        wait_times.insert(0, 0)
        termino = sorted_list[0].get_chegada() + first_duracao
        terminos.insert(0, termino)
        self.__add_event__(sorted_list[0].get_chegada(), sorted_list[0].get_id(), 1, eventos)
        self.__add_event__(termino, sorted_list[0].get_id(), 2, eventos)
        self.__add_event__(termino, sorted_list[1].get_id(), 1, eventos)

        # But the others do
        for i in range(1, len(sorted_list)):
            wait_time = terminos[i - 1] - sorted_list[i].get_chegada()
            wait_times.insert(i, wait_time)
            termino = sorted_list[i].get_chegada() + wait_time + sorted_list[i].get_duracao()
            self.__add_event__(termino, sorted_list[i].get_id(), 2, eventos)
            if i != len(sorted_list) - 1:
                self.__add_event__(termino, sorted_list[i+1].get_id(), 1, eventos)
            terminos.insert(i, termino)

        output = self.__get_formatted_result_header__("Shortest Job First")
        output += self.__print_events(eventos)

        throughput = len(self.processos) / duracao_total
        output += self.__get_statistics__(0, 0, throughput, 0)
        return output

    def __add_event__(self, simulation_time: int, pid: int, event: int, events: dict):
        if simulation_time not in events:
            events[simulation_time] = list()
        events[simulation_time]\
            .append(self.__get_formatted_result__(simulation_time, pid, self.__tipos_evento__[event]))

    def __print_events(self, events: dict):
        events_output = ""
        for k, v in sorted(events.items()):
            lista_events = v
            for event in lista_events:
                events_output += event
        return events_output

    def __any_process_left__(self, remaining_times: list):
        for time in remaining_times:
            if time != 0:
                return True
        return False

    # Shortest Remaining Time
    def executar_srt(self):
        remaining_times = self.__get_remaining_times__()
        wait_times = list()
        terminos = list()

        duracao_total = 0
        for processo in self.processos:
            duracao_total += processo.get_duracao()

        # First process doesn't wait
        first_duracao = self.processos[0].get_duracao()
        # self.processos[0].set_duracao(0)
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
        output = self.__get_formatted_result_header__("Shortest Remaining Time")
        indice_processo_execucao = 0
        while instante_atual <= duracao_total:
            for i in range(0, len(self.processos)):
                processo = sorted_list[i]
                # Verificar se algum processo chegou neste instante
                if processo.chegada == instante_atual:
                    output += self.__get_formatted_result__(instante_atual, processo.pid, "Chegada")
                    if i > 0:
                        # Verificar se o novo processo tem menor custo do que o que está a ser executado
                        if remaining_times[i] < remaining_times[i-1]:
                            output += self.__get_formatted_result__(instante_atual, sorted_list[i-1], "Exit (suspensao")
                            indice_processo_execucao = i
                            # O novo processo é menor do que o que está a ser executado

                if i == 0 and instante_atual == processo.get_chegada():
                    output += self.__get_formatted_result__(instante_atual, processo.pid, "Execução")
                    indice_processo_execucao = i

                # Executar o processo atual
                remaining_times[indice_processo_execucao] -= 1

                # Verificar se o processo terminou neste instante
                if remaining_times[indice_processo_execucao] == 0:
                    output += self.__get_formatted_result__(instante_atual, processo.pid, "Exit")

                    # Verificar se outro processo pode iniciar no próximo instante
                    if ultimo_processo == len(sorted_list) - 1:
                        break
                    # proximo_processo = sorted_list[ultimo_processo + 1].get_id()
                    # indice_processo_execucao = ultimo_processo + 1
                    proximo_processo = sorted_list[ultimo_processo + 1].get_id()
                    if not self.__any_process_left__(remaining_times):
                        break
                    output += self.__get_formatted_result__(instante_atual, proximo_processo, "Execução")
                    # output += self.__get_formatted_result__(instante_atual, processo.pid, "Execução")
                    indice_processo_execucao = i

            instante_atual += 1
        # self.processos[0].set_duracao(first_duracao)
        throughput = len(self.processos) / duracao_total
        output += self.__get_statistics__(0, 0, throughput, 0)
        return output

    # Round Robin
    ## TODO: Make this work
    def executar_rr(self, quantum: int):
        wait_times = list()
        start_times = list()
        remaining_times = self.__get_remaining_times__()

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
        output = self.__get_formatted_result_header__("Round Robin")
        indice_processo_em_execucao = 0
        quantum_atual = 0
        while instante_atual <= duracao_total:

            for i in range(0, len(self.processos)):
                processo = self.processos[i]

                # Verificar se algum processo chegou neste instante
                if processo.chegada == instante_atual:
                    output += self.__get_formatted_result__(instante_atual, processo.pid, "Chegada")

                # Se for o primeiro processo, vamos executar
                if i == 0 and instante_atual == processo.get_chegada():
                    output += self.__get_formatted_result__(instante_atual, processo.pid, "Execução")
                    indice_processo_em_execucao = i

            if remaining_times[indice_processo_em_execucao] > 0:
                remaining_times[indice_processo_em_execucao] -= 1

            if remaining_times[indice_processo_em_execucao] == 0 or quantum_atual == quantum:
                processo = self.processos[indice_processo_em_execucao]
                # print( str(processo.pid) + " está sair com " + str(remaining_times[indice_processo_em_execucao]) +
                #        " e quantum " + str(quantum_atual))
                output += self.__get_formatted_result__(instante_atual, processo.pid, "Exit " +
                                                        str(remaining_times[indice_processo_em_execucao]))
                quantum_atual = 0

                # Verificar se outro processo pode iniciar no próximo instante
                if indice_processo_em_execucao == len(self.processos) - 1:
                    indice_processo_em_execucao = 0
                else:
                    indice_processo_em_execucao += 1
                proximo_processo = self.processos[indice_processo_em_execucao].get_id()
                output += self.__get_formatted_result__(instante_atual, proximo_processo, "Execução")

            if quantum_atual == quantum:
                quantum_atual = 0
            else:
                quantum_atual += 1
            instante_atual += 1
        throughput = len(self.processos) / duracao_total
        output += self.__get_statistics__(0, 0, throughput, 0)
        return output

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
        return "Algoritmo de escalonamento: " + algorithm_name + "\n" \
                 + "=============================================================\n" \
                 + "| Simulation Time\t| ID do Processo\t|\tEvento\t\t|\n"

    def __get_formatted_result__(self, instante: int, pid: int, evento: str):
        return "|\t\t" + str(instante) + "\t\t\t|\t\t" + str(pid) + "\t\t\t|\t" + evento + "\t\t|\n"

    def __get_statistics__(self,
                           tempo_medio: int,  # Tempo médio de resposta
                           turn_around: int,  # Turn Around Time
                           throughput: int,  # Throughput
                           utilizacao_cpu: int  # Taxa de Utilização do CPU
                           ):
        output = "Estatística da Simulação\n" \
                 + "========================================\n" \
                 + "Tempo médio de resposta: " + str(tempo_medio) + "\n" \
                 + "Turn Around Time: " + str(turn_around) + "\n" \
                 + "Throughput: " + str(round(throughput, 2)) + "\n" \
                 + "Taxa de Utilização do CPU: " + str(utilizacao_cpu) + "\n"
        return output
