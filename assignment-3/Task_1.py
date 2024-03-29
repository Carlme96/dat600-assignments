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
    def __init__(self, weight, node1, node2):
        self.weight = weight
        self.src = node1
        self.dst = node2


class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.sort_nodes()

        # For DAG
        self.dag_nodes = []
        self.top_sorted = []

    def sort_nodes(self):
        self.nodes = sorted(self.nodes, key=lambda x: x.value)

    def reset_nodes(self):
        for node in self.nodes:
            node.reset()

    def bfs(self, start):
        print("BFS process")
        print("-"*20)
        self.reset_nodes()
        queue = [start]
        time = 1
        start.visited = True
        start.start_time = time
        while queue:
            time += 1
            print(f"Current queue: {[node.value for node in queue]}")
            node = queue.pop(0)
            
            print(f"\nCurrent node: {node.value}, Has edges to: {[edge.dst.value for edge in node.edges]}")
            for edge in node.edges:
                if not edge.dst.visited:
                    print(f"Visiting node: {edge.dst.value} at time {time}")
                    edge.dst.start_time = time
                    edge.dst.visited = True
                    edge.dst.distance = node.distance + 1
                    edge.dst.parent = node
                    queue.append(edge.dst)
                else: 
                    print(f"Node {edge.dst.value} already visited")
            node.finished = True
            node.finish_time = time

    def print_bfs(self):
        print("BFS results")
        print("-"*20)
        for node in self.nodes:
            print(f"Node: {node.value} \tParent: {node.parent.value if node.parent else None} \tTime: {node.start_time}/{node.finish_time} \tDistance: {node.distance} ")
        print("-"*20)
        print("\n")

    

    def dfs(self):
        print("DFS process")
        print("-"*20)
        self.reset_nodes()
        time = 0
        for node in self.nodes:
            if not node.visited:
                time = self.dfs_visit(node, time)

    def dfs_visit(self, node, time):
        
        time += 1
        print(f"\nNode {node.value}: Discovered at time {time}")
        node.start_time = time
        node.visited = True
        for edge in node.edges:
            if not edge.dst.visited:
                print(f"Node {node.value}: Visiting {edge.dst.value}")
                edge.dst.parent = node
                time = self.dfs_visit(edge.dst, time)
            else:
                print(f"Node {node.value}: Node {edge.dst.value} already visited")
        node.finished = True
        time += 1
        node.finish_time = time
        print(f"\nNode {node.value}: Finished at time {time}")
        return time

    def print_dfs(self):
        print("DFS")
        print("-"*20)
        for node in self.nodes:
            print(f"Node: {node.value} \tParent: {node.parent.value if node.parent else None} \tTime: {node.start_time}/{node.finish_time}")
        print("-"*20)
        print("\n")

    def make_dag(self):
        self.dfs()
 
        self.dag_nodes = copy.deepcopy(self.nodes)
        for node in self.dag_nodes:
            for edge in node.edges:
                if edge.dst.finish_time > node.finish_time:
                    node.edges.remove(edge)

    def print_dag(self):
        print("DAG")
        print("-"*20)
        for node in self.dag_nodes:
            print(f"Node: {node.value} \tEdges: {[edge.dst.value for edge in node.edges]}")
        print("-"*20)
        print("\n")
        
    def topological_sort(self):
        self.top_sorted = []
        self.top_sorted = sorted(self.dag_nodes, key=lambda x: x.finish_time, reverse=True)

    def print_topological_sort(self):
        print("Topological Sort")
        print("-"*20)
        for node in self.top_sorted:
            print(f"Node: {node.value} \tTime: {node.finish_time} \tTo: {[edge.dst.value for edge in node.edges]}")
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
    H = Node("H")
    I = Node("I")
    J = Node("J")

    A.add_edge(Edge(1, A, B))

    B.add_edge(Edge(1, B, C))
    B.add_edge(Edge(1, B, D))

    C.add_edge(Edge(1, C, E))
    C.add_edge(Edge(1, C, F))

    D.add_edge(Edge(1, D, E))
    D.add_edge(Edge(1, D, F))

    E.add_edge(Edge(1, E, F))
    E.add_edge(Edge(1, E, G))
    E.add_edge(Edge(1, E, J))

    F.add_edge(Edge(1, F, B))
    F.add_edge(Edge(1, F, G))
    F.add_edge(Edge(1, F, H))
    F.add_edge(Edge(1, F, J))

    H.add_edge(Edge(1, H, I))

    J.add_edge(Edge(1, J, I))

    # task 1 d
    I.add_edge(Edge(1, I, C))
    C.add_edge(Edge(1, C, A))

    graph = Graph([A, B, C, D, E, F, G, H, I, J])

    graph.bfs(A)
    graph.print_bfs()

    graph.dfs()
    graph.print_dfs()

    graph.make_dag()
    graph.print_dag()

    graph.topological_sort()
    graph.print_topological_sort()