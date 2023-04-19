from threading import Thread

def ordem_crescente():
    for i in range(1,501):
        print(i)

def ordem_decrescente():
    for j in range(500,0,-1):
        print(j)


if __name__ == '__main__':

    t1=Thread(target= ordem_crescente)
    t2=Thread(target= ordem_decrescente)

t1.start()
t1.join()

t2.start()
t2.join()