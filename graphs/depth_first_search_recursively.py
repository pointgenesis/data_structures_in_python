class Node:

    def __init__(self, name):
        self.name = name
        self.adjacency_list = []
        self.visited = False


def depth_first_search(node):
    print(node.name)
    node.visited = True
    for neighbor in node.adjacency_list:
        if not neighbor.visited:
            depth_first_search(neighbor)


def main():
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")

    node1.adjacency_list.append(node2)
    node1.adjacency_list.append(node3)
    node2.adjacency_list.append(node4)
    node4.adjacency_list.append(node5)

    depth_first_search(node1)


if __name__ == '__main__':
    main()
