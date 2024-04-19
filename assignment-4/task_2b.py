from pulp import LpMinimize, LpProblem, LpVariable, getSolver, LpStatus, value, allcombinations, lpSum, LpMaximize

model = LpProblem(name="linear_programming", sense=LpMaximize)

solver = getSolver("PULP_CBC_CMD")

verteces = ["s", "1", "2", "3", "4", "5", "t"]

edges = {
    "s1": 14,
    "s2": 25,
    "13": 3,
    "14": 21,
    "23": 13,
    "25": 7,
    "13": 3,
    "31": 6,
    "35": 15,
    "43": 10,
    "4t": 20,
    "54": 5,
    "5t": 10
}

E = LpVariable.dicts("E", edges.keys(), lowBound=0, cat="Continous")

model += E["s1"] + E["s2"]

for edge in edges:
    model += E[edge] <= edges[edge]

for vertex in verteces[1:-1]:
    in_edges = [edge for edge in edges if edge[1] == vertex]
    out_edges = [edge for edge in edges if edge[0] == vertex]
    model += lpSum([E[edge] for edge in in_edges]) == lpSum([E[edge] for edge in out_edges])



results = model.solve(solver=solver)

print(f'Maximum flow: z = {value(model.objective)}')
print([f"{edge} = {value(E[edge])}" for edge in edges])

