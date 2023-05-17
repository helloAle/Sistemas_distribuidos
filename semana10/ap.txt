import threading

def calcular_soma(vetor, inicio, fim):
    soma = sum(vetor[inicio:fim])
    print(f"Soma da thread {threading.current_thread().name}: {soma}")

vetor = list(range(1, 101))
tamanho_parte = len(vetor) // 4

threads = []
for i in range(4):
    inicio = i * tamanho_parte
    fim = (i + 1) * tamanho_parte if i < 3 else len(vetor)
    thread = threading.Thread(target=calcular_soma, args=(vetor, inicio, fim))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

soma_total = sum(vetor)
print(f"Soma total: {soma_total}")
