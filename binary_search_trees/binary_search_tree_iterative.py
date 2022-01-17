from typing import List


class Node:
    def __init__(self, data_point: int) -> None:
        self.data_point: int = data_point
        self.left_child: Node = None
        self.right_child: Node = None
        self.parent: Node = None


class BinarySearchTreeComparator:
    def compare(self, node1: Node, node2: Node) -> bool:
        if not node1 or not node2:
            return node1 == node2

        if node1.data_point != node2.data_point:
            return False

        return self.compare(node1.left_child, node2.left_child) and self.compare(node1.right_child, node2.right_child)


class BinarySearchTree:
    def __init__(self, debug: bool = False) -> None:
        self.root_node = None
        self.item_count = 0
        self.debug = debug

    def find_node(self, value: int, node: Node = None) -> Node:
        if node is None:
            node = self.root_node

        if value == node.data_point:
            return node
        else:
            if value > node.data_point and node.right_child is not None:
                # go right
                node = node.right_child
            elif value < node.data_point and node.left_child is not None:
                # go left
                node = node.left_child
            else:
                print(f'value: {value} not found in the tree') if self.debug else None
                return None
            return self.find_node(value, node)

    def min_valued_node(self, current_node: Node = None) -> Node:
        if current_node is None:
            current_node = self.root_node

        while True:
            if current_node is None:
                print(f'Tree is not initialized') if self.debug else None
                return None
            elif current_node.left_child is None:
                return current_node
            else:
                current_node = current_node.left_child

    def min_value(self, current_node: Node = None) -> int:
        if current_node is None:
            current_node = self.root_node

        while True:
            if current_node is None:
                print(f'Tree is not initialized')
                return -1
            elif current_node.left_child is None:
                return current_node.data_point
            else:
                current_node = current_node.left_child

    def max_valued_node(self, current_node: Node = None) -> Node:
        if current_node is None:
            current_node = self.root_node

        while True:
            if current_node is None:
                print(f'Tree is not initialized')
                return None
            elif current_node.right_child is None:
                return current_node
            else:
                current_node = current_node.right_child

    def max_value(self, current_node: Node = None) -> int:
        if current_node is None:
            current_node = self.root_node

        while True:
            if current_node is None:
                print(f'Tree is not initialized')
                return -1
            elif current_node.right_child is None:
                return current_node.data_point
            else:
                current_node = current_node.right_child

    def insert_node(self, data_point: int) -> None:
        new_node = Node(data_point)
        if self.root_node is None:
            self.root_node = new_node
            self.item_count += 1
            print(f'inserted {data_point} at root node') if self.debug else None
        else:
            current_node = self.root_node
            while True:
                if data_point < current_node.data_point:
                    # go left
                    if current_node.left_child is None:
                        # insert node here
                        current_node.left_child = new_node
                        new_node.parent = current_node
                        self.item_count += 1
                        print(f'inserted {data_point} as left child node of {current_node}') if self.debug else None
                        return
                    else:
                        current_node = current_node.left_child
                elif data_point > current_node.data_point:
                    # go right
                    if current_node.right_child is None:
                        # insert node here
                        current_node.right_child = new_node
                        new_node.parent = current_node
                        self.item_count += 1
                        print(f'inserted {data_point} as right child node of {current_node}') if self.debug else None
                        return
                    else:
                        current_node = current_node.right_child
                else:
                    raise ValueError(f'Invalid data_point: {data_point}')

    def delete(self, value: int) -> bool:
        #################################
        # TODO: STILL IN PROGRESS... this has been a motherfucker so far!
        #################################
        """
        Return True if a node with the given value was found and
        delete was successful; False, otherwise.
        """
        deleted_this_node = self.find_node(value)
        if deleted_this_node:
            if deleted_this_node.left_child:
                # go left - find max
                print('go left - find max') if self.debug else None
                left_max_node = self.max_valued_node(deleted_this_node.left_child)
                print(f'deleted_this_node.data_point: {deleted_this_node.data_point} left_max_node.data_point: {left_max_node.data_point}') if self.debug else None
                print(f'left_max_node.parent.data_point: {left_max_node.parent.data_point}') if self.debug else None

                if deleted_this_node.parent:
                    if deleted_this_node.parent.left_child and deleted_this_node.parent.left_child == deleted_this_node:
                        deleted_this_node.parent.left_child = left_max_node  # UNTESTED <<<<<<<<<<<<<<<<<<<<
                    elif deleted_this_node.parent.right_child and deleted_this_node.parent.right_child == deleted_this_node:
                        deleted_this_node.parent.right_child = left_max_node  # UNTESTED <<<<<<<<<<<<<<<<<<<<
                    else:
                        print(f'WARNING: THIS SHOULD NOT HAPPEN')
                    left_max_node.left_child = deleted_this_node.left_child
                    left_max_node.right_child = deleted_this_node.right_child
                    if left_max_node.parent.right_child == left_max_node:
                        left_max_node.parent.right_child = None

                    deleted_this_node.right_child.parent = left_max_node
                    print(f'data_point: {deleted_this_node.data_point}')
                    print(f'right_child.data_point: {deleted_this_node.right_child.data_point}')
                    print(f'left_child.data_point: {deleted_this_node.left_child.data_point}')
                    deleted_this_node.left_child.parent = left_max_node

                else:
                    # This is the root node
                    left_max_node.left_child = deleted_this_node.left_child
                    left_max_node.right_child = deleted_this_node.right_child
                    if left_max_node.parent.right_child == left_max_node:
                        left_max_node.parent.right_child = None
                    if left_max_node.parent.left_child == left_max_node:
                        left_max_node.parent.left_child = None

                    deleted_this_node.right_child.parent = left_max_node
                    deleted_this_node.left_child.parent = left_max_node

                    self.root_node = left_max_node

            elif deleted_this_node.right_child:
                # go right - find min
                print('go right - find min') if self.debug else None
                right_min_node = self.min_valued_node(deleted_this_node.right_child)
                print(f'deleted_this_node.data_point: {deleted_this_node.data_point} right_min_node.data_point: {right_min_node.data_point}') if self.debug else None

                if deleted_this_node.parent:
                    if deleted_this_node.parent.left_child and deleted_this_node.parent.left_child == deleted_this_node:
                        deleted_this_node.parent.left_child = None
                    elif deleted_this_node.parent.right_child and deleted_this_node.parent.right_child == deleted_this_node:
                        deleted_this_node.parent.right_child = None
                else:
                    print(f'WARNING: THIS SHOULD NOT HAPPEN')
                    # This is the root nodd
                    right_min_node.left_child = deleted_this_node.left_child
                    right_min_node.right_child = deleted_this_node.right_child
                    right_min_node.parent.right_child = None
                    deleted_this_node.right_child.parent = right_min_node
                    deleted_this_node.left_child.parent = right_min_node
                    self.root_node = right_min_node

            else:
                # childless node so delete
                # but must still update the parent
                if deleted_this_node.parent.left_child and deleted_this_node.parent.left_child == deleted_this_node:
                    deleted_this_node.parent.left_child = None
                elif deleted_this_node.parent.right_child and deleted_this_node.parent.right_child == deleted_this_node:
                    deleted_this_node.parent.right_child = None
                else:
                    raise ValueError('Current node''s parent does not have a reference to this node???')

            if deleted_this_node == self.root_node:
                self.root_node = None

            deleted_this_node = None
            self.item_count -= 1
            return True
        else:
            print(f'data_point not found: {value}')
            return False

    def traverse(self, values: List[int] = None, node: Node = None, ascending: bool = True) -> List[int]:
        if node is None:
            node = self.root_node

        if values is None:
            values = []

        if ascending:
            # default ascending traversal
            # visit left subtree
            if node.left_child:
                self.traverse(values, node.left_child)

            # capture data point
            values.append(node.data_point)

            # visit right subtree
            if node.right_child:
                self.traverse(values, node.right_child)
        else:
            # traversal in descending order
            # visit right subtree
            if node.right_child:
                self.traverse(values, node.right_child, False)

            # capture data point
            values.append(node.data_point)

            # visit left subtree
            if node.left_child:
                self.traverse(values, node.left_child, False)

        return values

def main():
    bst = BinarySearchTree(True)
    bst.insert_node(23)
    bst.insert_node(2)
    bst.insert_node(55)
    bst.insert_node(12)
    bst.insert_node(13)
    bst.insert_node(6)
    bst.insert_node(7)
    bst.insert_node(44)
    bst.insert_node(31)
    print(bst.traverse(ascending=False))
    print(bst.traverse())
    print(f'parent of 12 -> {(bst.find_node(12)).parent.data_point}')
    print(f'left_child of 12 -> {(bst.find_node(12)).left_child.data_point}')
    print(f'right_child of 12 -> {(bst.find_node(12)).right_child.data_point}')
    print(f'parent of 6 -> {(bst.find_node(6)).parent.data_point}')

    print(f'max_value: {bst.max_value()}')
    print(f'min_value: {bst.min_value()}')
    print(f'item_count: {bst.item_count}')
    value = 2223
    node = bst.find_node(value)
    if node:
        print(f'node found with data_point: {node.data_point} ')
    else:
        print(f'node NOT FOUND with data_point: {value} ')

    bst_a = BinarySearchTree(True)
    bst_a.insert_node(23)
    bst_a.insert_node(2)
    bst_a.insert_node(55)
    bst_a.insert_node(12)
    bst_a.insert_node(13)

    bst_b = BinarySearchTree(True)
    bst_b.insert_node(23)
    bst_b.insert_node(2)
    bst_b.insert_node(55)
    bst_b.insert_node(12)
    bst_b.insert_node(13)

    comparator = BinarySearchTreeComparator()
    print(comparator.compare(bst_a.root_node, bst_b.root_node))
    print(comparator.compare(bst_a.root_node, None))
    print(comparator.compare(None, bst_b.root_node))


if __name__ == '__main__':
    main()
