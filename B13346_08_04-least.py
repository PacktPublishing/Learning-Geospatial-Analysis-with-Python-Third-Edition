"""
Provides a simple command-line-output
version of the least cost path solution
using randomly-generated notional arrays.
"""

import numpy as np


# Our A* search algorithm
def astar(start, end, h, g):
    closed_set = set()
    open_set = set()
    path = set()
    open_set.add(start)
    while open_set:
        cur = open_set.pop()
        if cur == end:
            return path
        closed_set.add(cur)
        path.add(cur)
        options = []
        y1 = cur[0]
        x1 = cur[1]
        if y1 > 0:
            options.append((y1-1, x1))
        if y1 < h.shape[0]-1:
            options.append((y1+1, x1))
        if x1 > 0:
            options.append((y1, x1-1))
        if x1 < h.shape[1]-1:
            options.append((y1, x1+1))
        if end in options:
            return path
        best = options[0]
        closed_set.add(options[0])
        for i in range(1, len(options)):
            option = options[i]
            if option in closed_set:
                continue
            elif h[option] <= h[best]:
                best = option
                closed_set.add(option)
            elif g[option] < g[best]:
                best = option
                closed_set.add(option)
            else:
                closed_set.add(option)
        print(best, ", ", h[best], ", ", g[best])
        open_set.add(best)
    return []


# Width and height
# of grids
w = 5
h = 5

# Start location:
# Lower left of grid
start = (h-1, 0)

# End location:
# Top right of grid
dx = w-1
dy = 0

# Blank grid
a = np.zeros((w, h))

# Distance grid
dist = np.zeros(a.shape, dtype=np.int8)

# Calculate distance for all cells
for y, x in np.ndindex(a.shape):
    dist[y][x] = abs((dx-x)+(dy-y))

# "Terrain" is a random value between 1-16.
# Add to the distance grid to calculate
# The cost of moving to a cell
cost = np.random.randint(1, 16, (w, h)) + dist

print("COST GRID (Value + Distance)")
print(cost)
print()
print("(Y, X), HEURISTIC, DISTANCE")

# Find the path
path = astar(start, (dy, dx), cost, dist)
print()

# Create and populate the path grid
path_grid = np.zeros(cost.shape, dtype=np.uint8)
for y, x in path:
    path_grid[y][x] = 1
path_grid[dy][dx] = 1

print("PATH GRID: 1=path")
print(path_grid)
