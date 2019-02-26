from Processo import Processo


class Programa:
    def gerar_lista_processos(self, quantidade: int):
        processos = list()
        for i in range(0, quantidade):
            processos.append(Processo())
        return processos
