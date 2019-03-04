1. Um processo é um programa em execução.

2. BCP (Bloco de Controlo de Processos) é uma estrutura de dados que armazena dados de processos para
 simplificar o seu escalonamento. Tipicamente contém informações como Identificação, Prioridade, Estado, etc.
 
3. Diz-se que um processo sofre preempção quando a sua execução na CPU é interrompida para a execução de outro processo.

4. Turnaround time é o tempo que um processo leva para chegar ao fim.

   Tempo de espera é o tempo que um processo fica em modo de espera.
   
   Throughput é o número de processos processados num intervalo de tempo.
   
5. No algoritmo de escalonamento Shortest Job First, escolhe-se sempre o processo que tiver menor duração
 para ser executado. Este algoritmo é não-preemptivo, o que significa que mesmo se chegar um processo com duração menor
 do que aquele que está a ser executado, este não será interrompido.   

6. O algoritmo de escalonamento Shortest Remaining Time First é uma variação preemptiva do Shortest Job First.
 Escolhe-se sempre o processo que tiver menor duração para ser executado. Mas se chegar um processo com duração menor
 do que aquele que está a ser executado, este será interrompido para que o novo processo possa ser executado.
 
7. No algoritmo de escalonamento por Prioridade, é escolhido sempre o processo que tiver maior prioridade.
 Este algoritmo pode ou não ser preemptivo.
 
8. O Round-Robin é um algoritmo de escalonamento preemptivo, em que todos processos recebem o mesmo intervalo de tempo
 (quantum) para serem executados. Quando o quantum de um processo termina, esse processo é suspenso, para que o próximo
 processo seja executado.
 
9.    