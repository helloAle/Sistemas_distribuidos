import threading


# Matriz 5x5 de números inteiros
matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

# Função que calcula a soma dos valores de uma linha da matriz
def sum_row(row):
    return sum(row)

# Lista para armazenar os resultados das somas de cada linha
results = []

# Lista de threads para executar o cálculo das somas das linhas em paralelo
threads = []

# Loop para criar as threads e iniciar a execução do cálculo de cada linha
for row in matrix:
    t = threading.Thread(target=lambda r: results.append(sum_row(r)), args=(row,))
    threads.append(t)
    t.start()

# Aguardando todas as threads terminarem a execução
for t in threads:
    t.join()

# Imprimindo os resultados das somas de cada linha
print(results)
