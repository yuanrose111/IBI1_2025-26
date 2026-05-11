
# Create 100x100 grid
# Start with one infected cell
# For each step:
#     Infect neighbors
#     Recover infected cells
#     Update grid
# Show heatmap


import numpy as np
import matplotlib.pyplot as plt


size = 100
beta = 0.3
gamma = 0.05
time_steps = 100

# Initialize grid: 0=susceptible, 1=infected, 2=recovered
grid = np.zeros((size, size), dtype=int)
x, y = np.random.choice(size, 2)
grid[x, y] = 1

# 8 neighbors
neighbors = [(-1,-1), (-1,0), (-1,1),
             (0,-1),          (0,1),
             (1,-1),  (1,0), (1,1)]

plt.figure(figsize=(10,8))

for step in range(time_steps + 1):
    if step % 20 == 0:
        plt.subplot(2, 3, step//20 + 1)
        plt.imshow(grid, cmap='viridis', interpolation='nearest')
        plt.title(f'Time {step}')
        plt.axis('off')

    new_grid = grid.copy()
    infected_cells = np.argwhere(grid == 1)

    for (i, j) in infected_cells:
        # Infect neighbors
        for di, dj in neighbors:
            ni, nj = i + di, j + dj
            if 0 <= ni < size and 0 <= nj < size:
                if new_grid[ni, nj] == 0 and np.random.rand() < beta:
                    new_grid[ni, nj] = 1

        
        if np.random.rand() < gamma:
            new_grid[i, j] = 2

    grid = new_grid

plt.tight_layout()
plt.savefig('spatial_SIR.png')
plt.show()