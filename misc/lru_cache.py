from typing import KeysView, Any


class Node:
    def __init__(self, key: str, data: object) -> None:
        self.key: str = key
        self.data: object = data
        self.previous: Node = None
        self.next: Node = None


class LinkedList:
    def __init__(self) -> None:
        self.items = 0
        self.head: Node = None
        self.tail: Node = None

    def insert(self, node: Node) -> None:
        self.items += 1
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
        self.items -= 1
        self.tail = previous

    def delete(self, node: Node) -> None:
        previous_node: Node = node.previous
        next_node: Node = node.next
        if previous_node is not None:
            previous_node.next = next_node

        if next_node is not None:
            next_node.previous = previous_node

        del node
        self.items -= 1

    def traverse(self) -> list:
        values = []
        node = self.head

        while True:
            values.append(node.key)
            if node.next is not None:
                node = node.next
            else:
                return values


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache_references = {}
        self.linked_list_cache = LinkedList()

    def memoize(self, key: str, value: object):
        if self.linked_list_cache.items == self.capacity:
            del self.cache_references[self.linked_list_cache.tail.key]
            self.linked_list_cache.delete_tail()

        node = Node(key, value)
        self.linked_list_cache.insert(node)
        self.cache_references[key] = node

    def recall(self, key) -> object:

        node = self.cache_references[key]
        self.linked_list_cache.delete(node)
        self.linked_list_cache.insert(node)
        self.cache_references[key] = node

        return node.data

    def keys(self) -> KeysView[Any]:
        return self.cache_references.keys()


def main():
    # node = Node('travis')
    # node1 = Node('pete')
    # node2 = Node('fred')

    # linked_list = LinkedList()
    # linked_list.insert(node)
    # linked_list.insert(node1)
    # linked_list.insert(node2)
    #
    # print(linked_list.traverse())
    # print(linked_list.head.key)
    # print(linked_list.tail.key)
    #
    # linked_list.delete(node1)
    # print(linked_list.traverse())
    #
    # linked_list.delete_tail()
    # print(linked_list.traverse())

    lru_cache = LRUCache(10)
    lru_cache.memoize("travis", "travis lee steinmetz")
    lru_cache.memoize("lee", "Lee Leigh Lea")
    lru_cache.memoize("germany", "Germany Deutschland")
    lru_cache.memoize("france", "France Gaul")

    print(lru_cache.recall("travis"))
    print(lru_cache.keys())
    print(lru_cache.recall('travis'))
    for key in lru_cache.keys():
        print(f'{lru_cache.recall(key)}')

    print(lru_cache.linked_list_cache.items)

    for value in range(100):
        lru_cache.memoize(str(value), value)

    print(lru_cache.linked_list_cache.items)

    for key in lru_cache.keys():
        print(f'{lru_cache.recall(key)}')


if __name__ == '__main__':
    main()
