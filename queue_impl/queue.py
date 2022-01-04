from typing import Any


class Queue:
    """
    This implementation uses a list as the storage mechanism. A more efficient solution would use a doubly linked list.
    The doubly linked list allows for O(1) time complexity for the enqueue and dequeue operations.
    """
    def __init__(self):
        self.queue = []

    def enqueue(self, data_point: Any) -> None:
        self.queue.append(data_point)

    def dequeue(self) -> Any:
        data_point = None
        if not self.is_empty():
            data_point = self.queue[0]
            del self.queue[0]
        return data_point

    def peek(self) -> Any:
        data_point = None
        if not self.is_empty():
            data_point = self.queue[0]
        return data_point

    def is_empty(self) -> bool:
        return len(self.queue) == 0


if __name__ == '__main__':
    # TODO: implement the following as unittest methods
    queue_obj = Queue()

    print(f'Is the queue empty: {queue_obj.is_empty()}')

    queue_obj.enqueue("travis")
    print(f'Is the queue empty: {queue_obj.is_empty()}')

    queue_obj.dequeue()
    print(f'Is the queue empty: {queue_obj.is_empty()}')

    print(queue_obj.peek())

    queue_obj.enqueue("1")
    queue_obj.enqueue("2")
    queue_obj.enqueue("3")

    while not queue_obj.is_empty():
        print(queue_obj.peek())
        queue_obj.dequeue()

    print(f'Is the queue empty: {queue_obj.is_empty()}')
