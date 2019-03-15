# PARTE I
O objectivo da parte I é proporcional aprendizagem com base a de aplicação práctica de conceitos
aprendidos nas aulas relacionados com gestão de processos e memórias.
Devendo o estudante, para as linhas (3 e 4) descrever sumariamente:

 - Os procedimentos executados,
 - Evidências de execução e resultados,
 - Conclusões e lições aprendidas.

Para este trabalho será necessário o uso de um sistema Linux, sendo se recomenda virtualização
usando o VirtualBox para os que não possuem em seu computador pessoal.
No seguinte trabalho será usado as ferramentas de monitoramento nativas do sistema Linux,
respectivamente:
 - **strace** – monitoramento de execução de aplicações
 - **time** – providências estatísticas sobre utilização de recursos do computador por uma aplicação.
 
1. Crie um programa que seja IO-bound em Python3, o programa ao iniciar deve imprimir o ID do
utilizador que está a executar o programa.(usando a função getuid da biblioteca os)
2. Crie um programa que seja CPU-bound em Python3, o programa ao iniciar deve imprimir o PID
do processo que está a ser executado. (usando a função getpid da biblioteca os)
3. Usando a ferramenta strace (http://man7.org/linux/man-pages/man1/strace.1.html), capturar
as estatísticas de execução dos programas da linha 1 e 2.
4. Usando a ferramenta time (https://linux.die.net/man/1/time) deve capturar estatísticas de uso
de recurso em cada um dos programas desenvolvidos (linha 1 e 2), o tempo total de execução,
trocas de contexto voluntárias e trocas de contexto involuntárias. **Nota:** O código fonte das linhas 1 e 2 devem
 estar devidamente comentadas.
 
# PARTE II
Pretende-se com a parte II do trabalho, que os estudantes tenham noção de básicas das ferramentas
de monitoramento e administração dos sistemas operativos Microsoft Windows.
Para parte II do trabalho, o estudante deverá para as linhas (4 e 5) descrever sumariamente:
 - Os procedimentos executados,
 - Evidências de execução e resultados,
 - Conclusões e lições aprendidas.

1. Desenvolva um programa em Python3 que soma números primos em loop infinito, até que o
utilizador pressione a tecla “c”. Devendo mostrar na tela o número de vezes que somou, o
último número primo que foi somado e o resultado da soma.
2. Desenvolva um programa que executa uma tarefa, a linguagem de programação a sua escolha.
3. Descreva funcionamento e as funcionalidades da ferramenta “Resource Monitor”,
“Performance Monitor” e “Task Scheduler” do Microsoft Windows.
4. Execute o programa da linha 1 e monitore a execução do programa com base nas ferramentas
“Resource Monitor” e “Performance Monitor”.
5. Usando a ferramenta de “Task Scheduler”, agende a execução do programa criado na linha 2
para ser executado todos os dias as 20h.
