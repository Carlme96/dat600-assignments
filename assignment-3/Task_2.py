import copy

class Node:
    def __init__(self, value):
        self.value = value
        

class Edge:
    def __init__(self, weight, node1, node2):
        self.weight = weight
        self.src = node1
        self.dst = node2


class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.edges = []

    def add_edge(self, edge):
        self.edges.append(edge)

    def find_set(self, node, trees):
        for tree in trees:
            if node in tree:
                return tree
        return None

    def minimal_spanning_tree(self):
        self.edges = sorted(self.edges, key=lambda x: x.weight)
        print([f"({edge.src.value}, {edge.dst.value}) w: {edge.weight}" for edge in self.edges])
        total_weight = 0
        trees = []
        for node in self.nodes:
            trees.append({node})

        for edge in self.edges:
            set1 = self.find_set(edge.src, trees)
            set2 = self.find_set(edge.dst, trees)
            if set1 != set2:
                trees.remove(set1)
                trees.remove(set2)
                trees.append(set1.union(set2))
                total_weight += edge.weight
                print(f"({edge.src.value}, {edge.dst.value}) w: {edge.weight}")
        print(f"Total weight: {total_weight}")

    def minimal_spanning_tree_max_edges(self, max):
        all_edges = sorted(self.edges, key=lambda x: x.weight)
        print([f"({edge.src.value}, {edge.dst.value}) w: {edge.weight}" for edge in all_edges])

        new_edges = []
        count = {node.value: 0 for node in self.nodes}
        for edge in all_edges:
            count[edge.src.value] += 1
            count[edge.dst.value] += 1
            if count[edge.src.value] <= max and count[edge.dst.value] <= max:
                new_edges.append(edge)

        self.edges = new_edges
        print([f"({edge.src.value}, {edge.dst.value}) w: {edge.weight}" for edge in self.edges])

        total_weight = 0
        trees = []
        for node in self.nodes:
            trees.append({node})

        for edge in self.edges:
            set1 = self.find_set(edge.src, trees)
            set2 = self.find_set(edge.dst, trees)
            if set1 != set2:
                trees.remove(set1)
                trees.remove(set2)
                trees.append(set1.union(set2))
                total_weight += edge.weight
                print(f"({edge.src.value}, {edge.dst.value}) w: {edge.weight}")
        print(f"Total weight: {total_weight}")

def example():
    A = Node("A")
    B = Node("B")
    C = Node("C")
    D = Node("D")
    E = Node("E")
    F = Node("F")
    G = Node("G")
    H = Node("H")
    I = Node("I")
    
    graph = Graph([A, B, C, D, E, F, G, H, I])

    graph.add_edge(Edge(4, A, B))
    graph.add_edge(Edge(8, A, H))
    graph.add_edge(Edge(8, B, C))
    graph.add_edge(Edge(11, B, H))
    graph.add_edge(Edge(7, C, D))
    graph.add_edge(Edge(4, C, F))
    graph.add_edge(Edge(2, C, I))
    graph.add_edge(Edge(14, D, F))
    graph.add_edge(Edge(9, D, E))
    graph.add_edge(Edge(10, E, F))
    graph.add_edge(Edge(2, F, G))
    graph.add_edge(Edge(1, G, H))
    graph.add_edge(Edge(6, G, I))
    graph.add_edge(Edge(7, H, I))

    graph.minimal_spanning_tree()

def task_a():
    A = Node("A")
    B = Node("B")
    C = Node("C")
    D = Node("D")
    E = Node("E")
    F = Node("F")
    G = Node("G")
    H = Node("H")

    graph = Graph([A, B, C, D, E, F, G, H])

    graph.add_edge(Edge(5, A, B))
    graph.add_edge(Edge(1, A, D))

    graph.add_edge(Edge(4, B, D))
    graph.add_edge(Edge(8, B, H))

    graph.add_edge(Edge(2, D, C))
    graph.add_edge(Edge(2, D, E))
    graph.add_edge(Edge(4, D, F))

    graph.add_edge(Edge(6, C, G))

    graph.add_edge(Edge(8, E, H))

    graph.add_edge(Edge(9, F, G))
    graph.add_edge(Edge(7, F, H))

    graph.minimal_spanning_tree()


def task_b():
    A = Node("A")
    B = Node("B")
    C = Node("C")
    D = Node("D")
    E = Node("E")
    F = Node("F")
    G = Node("G")
    H = Node("H")

    graph = Graph([A, B, C, D, E, F, G, H])

    graph.add_edge(Edge(5, A, B))
    graph.add_edge(Edge(1, A, D))

    graph.add_edge(Edge(4, B, D))
    graph.add_edge(Edge(8, B, H))

    graph.add_edge(Edge(2, D, C))
    graph.add_edge(Edge(2, D, E))
    graph.add_edge(Edge(4, D, F))

    graph.add_edge(Edge(6, C, G))

    graph.add_edge(Edge(8, E, H))

    graph.add_edge(Edge(9, F, G))
    graph.add_edge(Edge(7, F, H))

    graph.minimal_spanning_tree_max_edges(3)

def task_b_counter():
    # Increasing A-B to w=20
    # Increasing B-H to w=20
    # Max edges algorithm removes D to B, which is not optimal
    # Removing D-C and D-F gives a lower total weigth

    A = Node("A")
    B = Node("B")
    C = Node("C")
    D = Node("D")
    E = Node("E")
    F = Node("F")
    G = Node("G")
    H = Node("H")

    graph = Graph([A, B, C, D, E, F, G, H])

    # Increase A-B to w=20
    graph.add_edge(Edge(20, A, B))

    graph.add_edge(Edge(1, A, D))

    graph.add_edge(Edge(4, B, D))

    # Increase B-H to w=20
    graph.add_edge(Edge(20, B, H))

    graph.add_edge(Edge(2, D, C))
    graph.add_edge(Edge(2, D, E))
    graph.add_edge(Edge(4, D, F))

    graph.add_edge(Edge(6, C, G))

    graph.add_edge(Edge(8, E, H))

    graph.add_edge(Edge(9, F, G))
    graph.add_edge(Edge(7, F, H))

    print("-"*20)
    graph.minimal_spanning_tree_max_edges(3)
    print("-"*20)
    print("\n")

    A = Node("A")
    B = Node("B")
    C = Node("C")
    D = Node("D")
    E = Node("E")
    F = Node("F")
    G = Node("G")
    H = Node("H")

    graph = Graph([A, B, C, D, E, F, G, H])

    # Increase A-B to w=20
    graph.add_edge(Edge(20, A, B))

    graph.add_edge(Edge(1, A, D))

    graph.add_edge(Edge(4, B, D))

    # Increase B-H to w=20
    graph.add_edge(Edge(20, B, H))

    # Remove D-C
    #graph.add_edge(Edge(2, D, C))
    graph.add_edge(Edge(2, D, E))
    
    # Remove D-F
    #graph.add_edge(Edge(4, D, F))

    graph.add_edge(Edge(6, C, G))

    graph.add_edge(Edge(8, E, H))

    graph.add_edge(Edge(9, F, G))
    graph.add_edge(Edge(7, F, H))

    graph.minimal_spanning_tree()

def task_c():
    # Switching A-B and F-G gives a lower total weight of 25
    A = Node("A")
    B = Node("B")
    C = Node("C")
    D = Node("D")
    E = Node("E")
    F = Node("F")
    G = Node("G")
    H = Node("H")

    graph = Graph([A, B, C, D, E, F, G, H])

    graph.add_edge(Edge(9, A, B))
    graph.add_edge(Edge(1, A, D))

    graph.add_edge(Edge(4, B, D))
    graph.add_edge(Edge(8, B, H))

    graph.add_edge(Edge(2, D, C))
    graph.add_edge(Edge(2, D, E))
    graph.add_edge(Edge(4, D, F))

    graph.add_edge(Edge(6, C, G))

    graph.add_edge(Edge(8, E, H))

    graph.add_edge(Edge(5, F, G))
    graph.add_edge(Edge(7, F, H))

    graph.minimal_spanning_tree()

if __name__ == "__main__":
    task_c()