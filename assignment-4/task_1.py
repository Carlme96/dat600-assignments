from pulp import LpMaximize, LpProblem, LpVariable, getSolver, LpStatus, value

model = LpProblem(name="linear_programming", sense=LpMaximize)

solver = getSolver("PULP_CBC_CMD")

x1 = LpVariable(name="x1", lowBound=0, cat="Continuous")
x2 = LpVariable(name="x2", lowBound=0, cat="Continuous")

model += (505/3)*x1 + (770/3)*x2

model += 15*x1 + 20*x2 <= 2400
model += 20*x1 + 30*x2 <= 2100
model += x1 >= 10


results = model.solve(solver=solver)

# print results
print(f'Max profit: z = {value(model.objective)}')
print(f'Solution: x1 = {value(x1)}, x2 = {value(x2)}')
