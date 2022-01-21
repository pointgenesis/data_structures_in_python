class Node:
    def __init__(self, key) -> None:
        self.key: str = key
        self.previous: Node = None
        self.next: Node = None


class LinkedList:
    def __init__(self) -> None:
        self.head: Node = None
        self.tail: Node = None

    def insert(self, node: Node) -> None:
        if self.head == None:
            self.head = node
            self.tail = node
            return

        node.next = self.head
        self.head.previous = node
        self.head = node

    def delete_tail(self) -> None:
        previous = self.tail.previous
        previous.next = None
        del self.tail

    def delete(self, node: Node) -> None:
        previous_node: Node = node.previous
        next_node: Node = node.next
        if previous_node is not None:
            previous_node.next = next_node

        if next_node is not None:
            next_node.previous = previous_node

        del node

    def traverse(self) -> list:
        values = []
        node = self.head

        while True:
            values.append(node.key)
            if node.next is not None:
                node = node.next
            else:
                return values


class CachedValues:
    def __init__(self):
        pass

    def insert(self, key, value):
        pass

    def get(self, key) -> object:
        return 't'


def main():
    node = Node('travis')
    node1 = Node('pete')
    node2 = Node('fred')

    linked_list = LinkedList()
    linked_list.insert(node)
    linked_list.insert(node1)
    linked_list.insert(node2)

    print(linked_list.traverse())
    print(linked_list.head.key)
    print(linked_list.tail.key)

    linked_list.delete(node1)
    print(linked_list.traverse())

    linked_list.delete_tail()
    print(linked_list.traverse())

if __name__ == '__main__':
    main()
