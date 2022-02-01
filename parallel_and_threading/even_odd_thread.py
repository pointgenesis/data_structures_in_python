import threading


def print_even_odd(s: str, start_index: int) -> None:
    for index in range(start_index, len(s), 2):
        print(f'{s[index]} {threading.current_thread().getName()}')


t1 = threading.Thread(target=print_even_odd, name='t1', args=('This is a text', 0,))
t2 = threading.Thread(target=print_even_odd, name='t2', args=('This is a text', 1,))

t1.start()
t2.start()

t1.join()
t2.join()
