from Processo import Processo


class Programa:

    def gerar_lista_processos(self, tempo_total: int):
        duracao = 0
        processos = list()
        # Adiciona processos aleatórios
        while True:
            processo = Processo()
            processos.append(processo)
            # Evitar criar processos que passam o tempo de simulação escolhido
            if duracao + (processo.get_duracao() * 2) > tempo_total:
                return processos
            duracao += processo.get_duracao()
