##atividade pratica:

Nesse código, o vetor de 100 posições é criado utilizando range(1, 101). Em seguida, o tamanho de cada parte é calculado dividindo o tamanho do vetor por 4.

Um loop é usado para criar e iniciar 4 threads, cada uma chamando a função calcular_soma com os índices corretos para cada parte do vetor.

Dentro da função calcular_soma, a soma dos elementos correspondentes à parte específica é calculada usando a função sum. A thread imprime seu próprio resultado.

Após o término das threads, a soma total de todos os elementos do vetor é calculada e impressa.