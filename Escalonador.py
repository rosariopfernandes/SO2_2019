class Escalonador:
    processos: list
    __tempo_total__: int

    __tipos_evento__ = {
        0: "Chegada",
        1: "Execução",
        2: "Exit"
    }

    def __init__(self, processos: list, tempo: int):
        self.__tempo_total__ = tempo
        self.processos = processos
        self.processos.sort(key=lambda p: p.chegada)

    def executar_fcfs(self):
        start_times = list()
        terminos = list()
        duracao_total = 0
        eventos = dict()
        turnarounds = list()

        for processo in self.processos:
            duracao_total += processo.get_duracao()
            # Adicionar as chegadas
            if processo.get_chegada() not in eventos:
                eventos[processo.get_chegada()] = list()
            eventos[processo.get_chegada()].append(str(self.__get_formatted_result__(processo.get_chegada(),
                                                                                     processo.pid, "Chegada")))

        # First process doesn't wait
        self.processos[0].set_tempo_espera(0)
        start_times.insert(0, self.processos[0].get_chegada())
        termino = self.processos[0].get_chegada() + self.processos[0].get_duracao()
        turnarounds.insert(0, termino)
        terminos.insert(0, termino)
        self.__add_event__(self.processos[0].get_chegada(), self.processos[0].get_id(), 1, eventos)
        self.__add_event__(termino, self.processos[0].get_id(), 2, eventos)

        # But the others do
        for i in range(1, len(self.processos)):
            wait_time = self.processos[i - 1].get_duracao() - self.processos[i].get_chegada()
            self.processos[i].set_tempo_espera(wait_time)

            start_time = start_times[i - 1] + self.processos[i - 1].get_duracao()
            start_times.insert(i, start_time)
            self.__add_event__(start_time, self.processos[i].get_id(), 1, eventos)

            termino = start_time + self.processos[i].get_duracao()
            turnarounds.insert(i, termino - self.processos[i].get_chegada())
            self.__add_event__(termino, self.processos[i].get_id(), 2, eventos)

        output = self.__get_formatted_result_header__("First Come First Serve")
        output += self.__print_events(eventos)

        throughput = len(self.processos) / duracao_total
        sum_turn_around_time = 0
        for time in turnarounds:
            sum_turn_around_time += time
        turn_around_time = sum_turn_around_time / len(self.processos)
        utilizacao = self.__get_utilizacao__(duracao_total)
        output += self.__get_statistics__(0, turn_around_time, throughput, utilizacao)
        return output

    # Shortest Job First
    def executar_sjf(self):
        terminos = list()
        turnarounds = list()
        duracao_total = 0
        eventos = dict()
        for processo in self.processos:
            duracao_total += processo.get_duracao()
            # Adicionar as chegadas
            if processo.get_chegada() not in eventos:
                eventos[processo.get_chegada()] = list()
            eventos[processo.get_chegada()].append(str(self.__get_formatted_result__(processo.get_chegada(),
                                                                                     processo.pid, "Chegada")))

        # First process doesn't wait
        first_duracao = self.processos[0].get_duracao()
        sorted_list = list(self.processos)
        sorted_list[0].set_duracao(0)
        sorted_list.sort(key=lambda p: p.get_duracao())
        self.processos[0].set_tempo_espera(0)
        termino = sorted_list[0].get_chegada() + first_duracao
        turnarounds.insert(0, termino)
        terminos.insert(0, termino)
        self.__add_event__(sorted_list[0].get_chegada(), sorted_list[0].get_id(), 1, eventos)
        self.__add_event__(termino, sorted_list[0].get_id(), 2, eventos)
        self.__add_event__(termino, sorted_list[1].get_id(), 1, eventos)

        # But the others do
        for i in range(1, len(sorted_list)):
            wait_time = terminos[i - 1] - sorted_list[i].get_chegada()
            self.processos[i].set_tempo_espera(wait_time)
            termino = sorted_list[i].get_chegada() + wait_time + sorted_list[i].get_duracao()
            turnarounds.insert(i, termino - self.processos[i].get_chegada())
            self.__add_event__(termino, sorted_list[i].get_id(), 2, eventos)
            if i != len(sorted_list) - 1:
                self.__add_event__(termino, sorted_list[i+1].get_id(), 1, eventos)
            terminos.insert(i, termino)

        output = self.__get_formatted_result_header__("Shortest Job First")
        output += self.__print_events(eventos)

        throughput = len(self.processos) / duracao_total
        sum_turn_around_time = 0
        for time in turnarounds:
            sum_turn_around_time += time
        turn_around_time = sum_turn_around_time / len(self.processos)
        utilizacao = self.__get_utilizacao__(duracao_total)
        output += self.__get_statistics__(0, turn_around_time, throughput, utilizacao)
        return output

    # Shortest Remaining Time
    def executar_srt(self):
        # TODO
        return

    # Round Robin
    def executar_rr(self, quantum: int):
        # TODO
        return

    # Funções Auxiliares

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

    def __get_utilizacao__(self, duracao: int):
        return (duracao * 100) / self.__tempo_total__

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
                 + "Turn Around Time: " + str(round(turn_around, 2)) + "\n" \
                 + "Throughput: " + str(round(throughput, 2)) + "\n" \
                 + "Taxa de Utilização do CPU: " + str(round(utilizacao_cpu, 2)) + "%\n"
        return output
