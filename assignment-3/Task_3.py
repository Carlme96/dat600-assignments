import copy

class Node:
    def __init__(self, value):
        self.value = value
        self.edges = []
        self.sort_edges()

        # For DFS and BFS
        self.visited = False
        self.finished = False
        self.parent = None
        self.distance = 0
        self.start_time = 0
        self.finish_time = 0

        # For grouping
        self.has_beat = set()


    def sort_edges(self):
        self.edges = sorted(self.edges, key=lambda x: x.dst.value)

    def add_edge(self, edge):
        self.edges.append(edge)
        self.sort_edges()

    def reset(self):
        self.visited = False
        self.finished = False
        self.parent = None
        self.distance = 0
        self.start_time = 0
        self.finish_time = 0

class Edge:
    def __init__(self, node1, node2):
        self.src = node1
        self.dst = node2


class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.sort_nodes()

        self.nodes_reversed = copy.deepcopy(self.nodes)
        self.champions = []
        self.has_beat = []
        self.groups = []

    def sort_nodes(self):
        self.nodes = sorted(self.nodes, key=lambda x: x.value)

    def reset_nodes(self):
        for node in self.nodes:
            node.reset()

    def reset_nodes_reversed(self):
        for node in self.nodes_reversed:
            node.reset()
    

    def dfs(self):
        self.reset_nodes()
        time = 0
        for node in self.nodes:
            if not node.visited:
                time = self.dfs_visit(node, time)

    def dfs_visit(self, node, time):
        time += 1
        node.start_time = time
        node.visited = True
        for edge in node.edges:
            if not edge.dst.visited:
                edge.dst.parent = node
                time = self.dfs_visit(edge.dst, time)
        node.finished = True
        time += 1
        node.finish_time = time
        return time

    def print_dfs(self):
        print("DFS")
        print("-"*20)
        for node in self.nodes:
            print(f"Node: {node.value} \tParent: {node.parent.value if node.parent else None} \tTime: {node.start_time}/{node.finish_time}")
        print("-"*20)
        print("\n")

    def dfs_champion(self):
        self.champions = []
        for node in self.nodes:
            self.reset_nodes()
            connections = self.dfs_visit_champion(node)
            print(f"Node {node.value} \tHas beat: {connections}")
            node.has_beat = copy.deepcopy(connections)
            if len(self.nodes) == len(connections):
                self.champions.append(node.value)

    def dfs_visit_champion(self, node):
        connections = set()
        connections.add(node.value)
        node.visited = True
        for edge in node.edges:
            if not edge.dst.visited:
                edge.dst.parent = node
                connections.add(edge.dst.value)
                connections = connections.union(self.dfs_visit_champion(edge.dst))
        node.finished = True
        return connections
    
    def print_dfs_champion(self):
        print("\nDFS Champions")
        print("-"*20)
        print(f"Champions: {self.champions}")
        print("-"*20)
        print("\n")

    def print_groups(self):
        print("Groups")
        print("-"*20)
        groups = []
        for node in self.nodes:
            found = False
            for group in groups:
                if node.has_beat == group[0].has_beat:
                    group.append(node)
                    found = True
                    break
            if not found:
                groups.append([node])

                
            print(f"Node: {node.value} \tHas beat: {node.has_beat}")

        print (f"Groups: {[[node.value for node in group] for group in groups]}")
        print("-"*20)
        print("\n")


if __name__ == "__main__":
    A = Node("A")
    B = Node("B")
    C = Node("C")
    D = Node("D")
    E = Node("E")
    F = Node("F")
    G = Node("G")

    A.add_edge(Edge(A, B))
    A.add_edge(Edge(A, D))

    B.add_edge(Edge(B, A))
    B.add_edge(Edge(B, C))

    D.add_edge(Edge(D, B))
    D.add_edge(Edge(D, C))

    C.add_edge(Edge(C, E))
    C.add_edge(Edge(C, F))

    E.add_edge(Edge(E, G))

    F.add_edge(Edge(F, E))

    G.add_edge(Edge(G, F))

    graph = Graph([A, B, C, D, E, F, G])

    graph.dfs_champion()
    graph.print_dfs_champion()
    graph.print_groups()
    