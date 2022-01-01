class Node:

    def __init__(self, data):
        self.data = data
        self.next_node = None
    # end __init__

# end class

class LinkedList:

    def __init__(self):
        self.head = None
        self.number_of_nodes = 0
    # end __init__

    def insert_at_head(self, data: str):
        node = Node(data)
        if self.head:
            node.next_node = self.head
            self.head = node
        else:
            self.head = node
        # end if
        self.number_of_nodes += 1
    # end def

    def insert_at_tail(self, data: str):
        node = Node(data)
        current_node = self.head
        while current_node.next_node:
            current_node = current_node.next_node
        # end while

        if not current_node.next_node:
            current_node.next_node = node
        # end if

        self.number_of_nodes += 1
    # end def

    def remove(self, data: str):
        current_node = self.head
        previous_node = None
        idx = 0
        while current_node and (current_node.data != data) and (idx < self.number_of_nodes):
            previous_node = current_node
            current_node = current_node.next_node
            idx += 1
        # end while

        if current_node and current_node.data == data:
            if previous_node:
                previous_node.next_node = current_node.next_node
            else:
                self.head = current_node.next_node
            current_node = None
            self.number_of_nodes -= 1
        else:
            print(f'No matching node with attribute ==> data: {data}')
        # end if
    # end def

    def to_array(self):
        current_node = self.head
        idx = 0
        array_list = []
        while idx < self.number_of_nodes:
            array_list.append(current_node.data)
            current_node = current_node.next_node
            idx += 1
        # end while
        return array_list
    # end def

# end class

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert_at_head("mike mike")
    linked_list.insert_at_head("bubba smith")
    linked_list.insert_at_head("jack nicholson")
    linked_list.insert_at_head("leonardo da vinci")
    linked_list.insert_at_head("geordi la forge")
    linked_list.insert_at_head("will riker")

    print(f'linked_list.to_array(): {linked_list.to_array()}')

    linked_list.insert_at_tail('joe bob')
    linked_list.insert_at_tail('chris robinson')

    print(f'linked_list.to_array(): {linked_list.to_array()} number of nodes: {linked_list.number_of_nodes}')

    linked_list.remove('jilly hilly')
    print(f'remove(jilly hilly) => linked_list.to_array(): {linked_list.to_array()} number of nodes: {linked_list.number_of_nodes}')

    linked_list.remove('mike mike')
    print(f'remove(mike mike) => linked_list.to_array(): {linked_list.to_array()} number of nodes: {linked_list.number_of_nodes}')

    linked_list.remove('will riker')
    print(f'remove(will riker) => linked_list.to_array(): {linked_list.to_array()} number of nodes: {linked_list.number_of_nodes}')

    linked_list.remove('jack nicholson')
    print(f'remove(jack nicholson) => linked_list.to_array(): {linked_list.to_array()} number of nodes: {linked_list.number_of_nodes}')