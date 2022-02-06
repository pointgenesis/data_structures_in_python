import threading

corrupted_value = 0


class DataPoint(object):
    def __init__(self):
        self.value = 0

    def increment_value(self):

        for _ in range(100000):
            global corrupted_value
            corrupted_value += 1

        for _ in range(100000):
            self.value += 1


def main():
    data_point = DataPoint()

    thread1 = threading.Thread(target=data_point.increment_value(), name='Thread-1')
    thread2 = threading.Thread(target=data_point.increment_value(), name='Thread-2')

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print(f'self.value: {data_point.value}')
    print(f'self.value: {corrupted_value}')


if __name__ == '__main__':
    main()
