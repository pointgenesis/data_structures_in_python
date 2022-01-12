from typing import List


class Node:
    def __init__(self, data):
        self.data = data
        self.previous_node = None
        self.next_node = None


class DoublyLinkedList:
    def __init__(self):
        self.item_count = 0
        self.head = None
        self.tail = None

    def _initial_insertion(self, node):
        self.head = node
        self.tail = node

    def insert_at_head(self, data):
        node = Node(data)

        if self.head is None:
            self._initial_insertion(node)

        self.head.previous_node = node
        node.next_node = self.head
        self.head = node

        self.item_count += 1

    def insert_at_tail(self, data):
        node = Node(data)

        if self.tail is None:
            self._initial_insertion(node)

        self.tail.next_node = node
        node.previous_node = self.tail
        self.tail = node

        self.item_count += 1


    def remove(self, data):
        node = self.head

        iteration = 0
        while node and iteration < self.item_count:
            if node.data == data:
                # remove node
                previous_node = node.previous_node
                next_node = node.next_node

                if previous_node:
                    previous_node.next_node = next_node
                else:
                    self.head = None

                if next_node:
                    next_node.previous_node = previous_node
                else:
                    self.tail = None

                self.item_count -= 1
                return

            node = node.next_node
            iteration += 1
        print(f'WARNING: Datapoint: {data} was not found')


    def to_array(self) -> List[str]:
        values = [""] * self.item_count

        node = self.head
        for idx in range(self.item_count):
            values[idx] = node.data
            node = node.next_node

        return values


def main():
    linked_list = DoublyLinkedList()
    linked_list.insert_at_head('travis')
    linked_list.insert_at_head('eric')
    linked_list.insert_at_head('greg')
    linked_list.insert_at_head('keith')
    linked_list.insert_at_head('kevin')
    linked_list.insert_at_head('james')
    print(linked_list.to_array())
    linked_list.insert_at_tail('spencer')
    linked_list.insert_at_tail('caleb')
    linked_list.insert_at_tail('jordan')
    linked_list.insert_at_tail('erin')
    print(linked_list.to_array())
    linked_list.remove('grdeg')
    print(linked_list.to_array())
    linked_list.remove('greg')
    print(linked_list.to_array())



if __name__ == '__main__':
    main()
