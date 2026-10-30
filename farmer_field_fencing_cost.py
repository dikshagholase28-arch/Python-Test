length = 50
breadth = 40
radius = 20
pi = 3.14
wire = 5
cost = 35

rectangle = 2 * (length + breadth)
circle = 2 * pi * radius

perimeter = rectangle + circle

total_wire = perimeter * wire
total_cost = total_wire * cost

print("Rectangle Perimeter:", rectangle)
print("Circle Circumference:", circle)
print("Total Wire Required:", total_wire)
print("Total Cost:", total_cost)