from typing import Any


class Stack:

    def __init__(self) -> None:
        self.stack_array = []

    def pop(self) -> Any:
        data_point = None
        if not self.is_empty():
            data_point = self.stack_array[-1]
            del self.stack_array[-1]
        return data_point

    def push(self, data_point: Any) -> Any:
        self.stack_array.append(data_point)

    def peek(self) -> Any:
        return None if self.is_empty() else self.stack_array[-1]

    def is_empty(self):
        return True if len(self.stack_array) == 0 else False


if __name__ == '__main__':
    # TODO: Convert the following into unittest methods
    my_stack = Stack()
    print(f'Is stack empty: {my_stack.is_empty()}')

    print(f'What is on top of the stack: {my_stack.peek()}')

    print(f'Push value (2) on to stack: {my_stack.push(2)}')
    print(f'What is on top of the stack: {my_stack.peek()}')

    print(f'Push value (4) on to stack: {my_stack.push(4)}')
    print(f'What is on top of the stack: {my_stack.peek()}')

    print(f'Push value (6) on to stack: {my_stack.push(6)}')
    print(f'What is on top of the stack: {my_stack.peek()}')

    print(f'Is stack empty: {my_stack.is_empty()}')

    print(f'Pop off top of stack: {my_stack.pop()}')
    print(f'What is on top of the stack: {my_stack.peek()}')

    print(f'Pop off top of stack: {my_stack.pop()}')
    print(f'What is on top of the stack: {my_stack.peek()}')

    print(f'Pop off top of stack: {my_stack.pop()}')
    print(f'What is on top of the stack: {my_stack.peek()}')

    print(f'Pop off top of stack: {my_stack.pop()}')
    print(f'What is on top of the stack: {my_stack.peek()}')

    print(f'Is stack empty: {my_stack.is_empty()}')
