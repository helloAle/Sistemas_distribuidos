# Importando a biblioteca threading para utilizar threads em Python
import threading

# Definindo a função count_up() para contar e imprimir de 1 a 500
def count_up():
    for i in range(1, 501):
        print(i)

# Definindo a função count_down() para contar e imprimir de 500 a 1
def count_down():
    for i in range(500, 0, -1):
        print(i)

# Criando uma nova thread (t1) e definindo a função target como count_up()
t1 = threading.Thread(target=count_up)

# Criando uma nova thread (t2) e definindo a função target como count_down()
t2 = threading.Thread(target=count_down)


# Iniciando a thread t1
t1.start()

# Iniciando a thread t2
t2.start()

# Aguardando o término da execução da thread t1 antes de continuar a execução do programa principal
t1.join()

# Aguardando o término da execução da thread t2 antes de continuar a execução do programa principal
t2.join()
