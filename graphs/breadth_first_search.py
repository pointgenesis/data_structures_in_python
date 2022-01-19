class Node:
    def __init__(self, name):
        self.name = name
        self.adjacency_list = []
        self.visited = False


def breadth_first_search(start_node):
    queue = [start_node]  # BFS is a FIFO algorithm, hence the queue

    while queue:
        actual_node = queue.pop(0)
        actual_node.visited = True
        print(actual_node.name)
        for neighbor in start_node.adjacency_list:
            if not neighbor.visited:
                queue.append(neighbor)


if __name__ == '__main__':
    mia = Node("Miami")
    nsu = Node("Ft. Lauderdale")
    unf = Node("Jacksonville")
    ucf = Node("Orlando")
    usf = Node("Tampa")
    # fsu = Node("Tallahassee")

    mia.adjacency_list.append(nsu)
    mia.adjacency_list.append(ucf)
    nsu.adjacency_list.append(ucf)
    ucf.adjacency_list.append(usf)

    breadth_first_search(mia)
