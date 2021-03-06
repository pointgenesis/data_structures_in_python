class Node:
    def __init__(self, value):
        self.value = value
        self.left_node = None
        self.right_node = None
    # end __init__
# end class

class BinarySearchTree:
    def __init__(self):
        self.root = None
    # end def

    def insert(self, data):
        new_node = Node(data)
        current_node = self.root
        if current_node is None:
            self.root = new_node
            print(f'Inserted root node => root: {data}')
        else:
            is_inserted = False
            while not is_inserted:
                if data < current_node.value:
                    if current_node.left_node:
                        current_node = current_node.left_node
                    else:
                        current_node.left_node = new_node
                        is_inserted = True
                        print(f'Inserted current_node: {current_node.value} => left_node: {data}')
                    # end if
                elif data > current_node.value:
                    if current_node.right_node:
                        current_node = current_node.right_node
                    else:
                        current_node.right_node = new_node
                        is_inserted = True
                        print(f'Inserted current_node: {current_node.value} => right_node: {data}')
                    # end if
                else:
                    raise ValueError(f'Invalid argument => data: {data}')
                # end if
            # end while
        # end if
    # end def

    def min(self):
        return self.min_from_node(self.root)

    def min_from_node(self, current_node):
        while current_node and current_node.left_node:
            current_node = current_node.left_node
        # end while
        if current_node:
            return current_node.value
        else:
            print(f'WARNING: Tree may not have been initialized.')
            return None

    def max(self):
        return self.max_from_node(self.root)

    def max_from_node(self, current_node):
        while current_node and current_node.right_node:
            current_node = current_node.right_node
        # end while

        if current_node:
            return current_node.value
        else:
            print(f'WARNING: Tree may not have been initialized')
            return None

    def remove(self, data):
        if self.root:
            self.remove_node(data, self.root)

    def remove_node(self, data, node):

        if node is None:
            return

        if data < node.data:
            self.remove_node(data, node.left_node)
        elif data > node.data:
            self.remove_node(data, node.right_node)
        else:

            if node.left_node is None and node.right_node is None:
                print("Removing a leaf node...%d" % node.data)

                parent = node.parent

                if parent is not None and parent.left_node == node:
                    parent.left_node = None
                if parent is not None and parent.right_node == node:
                    parent.right_node = None

                if parent is None:
                    self.root = None

                del node

            elif node.left_node is None and node.right_node is not None:  # node !!!
                print("Removing a node with single right child...")

                parent = node.parent

                if parent is not None:
                    if parent.left_node == node:
                        parent.left_node = node.left_node
                    if parent.rightChild == node:
                        parent.right_node = node.right_node
                else:
                    self.root = node.right_node

                node.right_node.parent = parent
                del node

            elif node.right_node is None and node.left_node is not None:
                print("Removing a node with single left child...")

                parent = node.parent

                if parent is not None:
                    if parent.left_node == node:
                        parent.left_node = node.left_node
                    if parent.right_node == node:
                        parent.right_node = node.left_node
                else:
                    self.root = node.left_node

                node.left_node.parent = parent
                del node

            else:
                print('Removing node with two children....')

                predecessor = self.get_predecessor(node.left_node)

                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp

                self.remove_node(data, predecessor)

    def get_predecessor(self, node):
        if node.right_node:
            return self.get_predecessor(node.right_node)

        return node

    def find_node(self, data, current_node):
        if current_node and current_node.value == data:
            print(f'found_it ==> {data}')
            return current_node
        elif current_node and current_node.value > data:
            # look through left node side
            print(f'looking for data: {data} through the left side of current_node.value: {current_node.value}')
            return self.find_node(data, current_node.left_node)
        elif current_node and current_node.value < data:
            # look through right nodes side
            print(f'looking for data: {data} through the right side of current_node.value: {current_node.value}')
            return self.find_node(data, current_node.right_node)
        else:
            return None
        # end if
    # end def

    def traverse_asc(self):
        asc_values = []
        return self.asc_order_from_node(self.root, asc_values)

    def asc_order_from_node(self, node: Node, asc_values: list):
        if node.left_node:
            self.asc_order_from_node(node.left_node, asc_values)

        asc_values.append(node.value)

        if node.right_node:
            self.asc_order_from_node(node.right_node, asc_values)

        return asc_values


    def traverse_desc(self):
        desc_values = []
        return self.desc_order_from_node(self.root, desc_values)

    def desc_order_from_node(self, node, desc_values):
        if node.right_node:
            self.desc_order_from_node(node.right_node, desc_values)
        print(f'node.value: {node.value}')
        desc_values.append(node.value)

        if node.left_node:
            self.desc_order_from_node(node.left_node, desc_values)

        return desc_values

# end class


if __name__ == '__main__':
    bst = BinarySearchTree()
    # values = [43, 25, 7, 12, 17, 99, 77, 44, 107, 91]
    values = [23, 2, 12, 6, 55, 44, 31]
    try:
        for value in values:
            bst.insert(value)

        print(f'min value: {bst.min()}')
        print(f'max value: {bst.max()}')

        print(f'asc values: {bst.traverse_asc()}')
        print(f'desc values: {bst.traverse_desc()}')

        bst.remove(12)
        print(f'desc values: {bst.traverse_desc()}')

    except ValueError as ve:
        print(f'ERROR: {ve}')
