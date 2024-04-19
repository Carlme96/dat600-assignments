from pulp import LpMinimize, LpProblem, LpVariable, getSolver, LpStatus, value, allcombinations, lpSum, LpMaximize

model = LpProblem(name="linear_programming", sense=LpMinimize)

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
    "35": 15,
    "43": 10,
    "4t": 20,
    "54": 5,
    "5t": 10
}

x = LpVariable.dicts("x", verteces, lowBound=0, cat="Binary")

E = LpVariable.dicts("E", edges.keys(), lowBound=0, cat="Binary")

model += lpSum([edges[edge]*E[edge] for edge in edges])

model += x["s"] == 1
model += x["t"] == 0

for edge in edges:
    print(x[edge[0]] - x[edge[1]] == E[edge])
    model += x[edge[0]] - x[edge[1]] == E[edge]



results = model.solve(solver=solver)

print(f'Minimal cut capacity: z = {value(model.objective)}')
print(f"At edges: {[edge for edge in edges if value(E[edge]) == 1]}")

