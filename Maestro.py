from datetime import datetime


class Maestro:

    def __get_result_str__(self, algorithm_name: str, results: list):
        output = "Algoritmo de escalonamento:" + algorithm_name + "\n" \
                 + "========================================\n" \
                 + "| " + "\n"  # TODO: Add headers once you find a nice way to print tabular data

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
                 + "Throughput: " + str(throughput) + "\n" \
                 + "Taxa de Utilização do CPU: " + str(utilizacao_cpu) + "\n"
        return output

    def __write_file__(self, content: str):
        today = datetime.now()
        formatted_date = today.strftime("%Y%m%d_%H%M")
        f = open("resultado_" + formatted_date + ".log", "x")
        f.write(content)
