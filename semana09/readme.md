#pa.py

##Explicação do código:

Primeiro, importamos a biblioteca threading.
Em seguida, definimos duas funções count_up() e count_down(), cada uma com um loop for que conta de forma crescente e decrescente, respectivamente, e exibe na tela o número atual.
Depois, criamos duas threads t1 e t2, passando como argumentos as funções count_up() e count_down(), respectivamente.
Em seguida, iniciamos as threads com os métodos start().
Por fim, usamos os métodos join() para esperar que as duas threads terminem antes que o programa termine.



#ap.py

##Explicação do código:

Primeiro, definimos a matriz 5x5 de números inteiros.
Em seguida, definimos a função sum_row() que calcula a soma dos valores de uma linha da matriz.
Criamos uma lista results para armazenar os resultados das somas de cada linha.
Criamos uma lista de threads threads para executar o cálculo das somas das linhas em paralelo.
Usamos um loop para criar as threads e iniciar a execução do cálculo de cada linha. Para cada linha da matriz, criamos uma nova thread passando como argumentos a função sum_row() e a linha correspondente da matriz. Usamos a função lambda para criar uma nova função anônima que recebe a linha como argumento e chama a função sum_row().
Adicionamos cada thread criada na lista threads.
Usamos outro loop para aguardar todas as threads terminarem a execução, usando o método join().
Por fim, imprimimos os resultados das somas de cada linha armazenados na lista results.