import threading

x = 0


def increment():
    global x
    x += 1


def operation():
    for _ in range(1000):
        increment()


thread1 = threading.Thread(target=operation(), name='Thread-1')
thread2 = threading.Thread(target=operation(), name='Thread-2')

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(x)
