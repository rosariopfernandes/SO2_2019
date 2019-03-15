from random import randint


class Processo:
    pid: int = 1
    chegada: int  # Horário de chegada
    duracao: int  # Previsão da Duração
    tempo_espera: int
    tempo_resposta: int

    def __init__(self):
        self.pid = Processo.pid
        self.chegada = randint(0, 9)
        self.duracao = randint(1, 9)
        self.tempo_espera = 0
        self.tempo_resposta = 0
        Processo.pid = Processo.pid + 1

    def get_id(self):
        return self.pid

    def get_chegada(self):
        return self.chegada

    def get_duracao(self):
        return self.duracao

    def get_tempo_espera(self):
        return self.tempo_espera

    def get_tempo_resposta(self):
        return self.tempo_resposta

    def set_id(self, pid: int):
        self.pid = pid

    def set_chegada(self, chegada: int):
        self.chegada = chegada

    def set_duracao(self, duracao: int):
        self.duracao = duracao

    def set_tempo_espera(self, tempo_espera: int):
        self.tempo_espera = tempo_espera

    def set_tempo_resposta(self, tempo_resposta: int):
        self.tempo_resposta = tempo_resposta
