"""
Implementation of Value Iteration Algorithm for Question 1
This version allows user input for grid size and goal position.
It performs value iteration.
After convergence, it prints the optimal policy using symbols.
Additionally, it uses matplotlib to plot a 2D visualization of the grid world with policy arrows.
Arrows indicate the optimal action: ^ (up), v (down), < (left), > (right), * (goal).
Run this code in a Python environment with matplotlib installed to see the plot.
"""
import matplotlib.pyplot as plt
import numpy as np 

# Get user inputs.
grid_size = int(input("Enter grid size (e.g., 5 for 5x5): "))
goal_i = int(input("Enter goal row (0 to {}): ".format(grid_size - 1))) 
goal_j = int(input("Enter goal column (0 to {}): ".format(grid_size - 1))) 
goal = (goal_i, goal_j) 

actions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 
action_symbols = ['U', 'D', 'L', 'R']
action_arrows = ['^', 'v', '<', '>'] 
gamma = 0.9 
threshold = 1e-4 

# Initialize value function V as grid_size x grid_size list of 0.0
V = [[0.0 for _ in range(grid_size)] for _ in range(grid_size)]

# Value iteration
while True:
    delta = 0  # Max change.
    for i in range(grid_size):
        for j in range(grid_size):
            if (i, j) == goal:
                continue
            v = V[i][j]
            max_val = float('-inf')
            for a in range(4):
                ni = i + actions[a][0]
                nj = j + actions[a][1]
                if 0 <= ni < grid_size and 0 <= nj < grid_size:
                    r = 10 if (ni, nj) == goal else -1
                    val = r + gamma * V[ni][nj]
                else:
                    r = -1
                    val = r + gamma * V[i][j]
                if val > max_val:
                    max_val = val
            V[i][j] = max_val
            delta = max(delta, abs(v - V[i][j]))
    if delta < threshold:
        break

# Extract optimal policy from value function
policy = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]
policy_arrows = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]  # For plotting.
for i in range(grid_size):
    for j in range(grid_size):
        if (i, j) == goal:
            policy[i][j] = 'G'
            policy_arrows[i][j] = '*'
            continue
        max_val = float('-inf')
        best_a = 0
        for a in range(4):
            ni = i + actions[a][0]
            nj = j + actions[a][1]
            if 0 <= ni < grid_size and 0 <= nj < grid_size:
                r = 10 if (ni, nj) == goal else -1
                val = r + gamma * V[ni][nj]
            else:
                r = -1
                val = r + gamma * V[i][j]
            if val > max_val:
                max_val = val
                best_a = a
        policy[i][j] = action_symbols[best_a]
        policy_arrows[i][j] = action_arrows[best_a]

# Print the optimal policy 
print("Optimal Policy:")
for row in policy:
    print(' '.join(row))

# Plot the 2D grid
fig, ax = plt.subplots() 
ax.set_xlim(0, grid_size) 
ax.set_ylim(0, grid_size) 
ax.set_xticks(np.arange(0, grid_size + 1, 1)) 
ax.set_yticks(np.arange(0, grid_size + 1, 1))
ax.grid(True)

# Add arrows
for i in range(grid_size):
    for j in range(grid_size):
        symbol = policy_arrows[i][j]
        ax.text(j + 0.5, grid_size - i - 0.5, symbol, ha='center', va='center', fontsize=20) 

# Mark goal
ax.text(goal_j + 0.5, grid_size - goal_i - 0.5, '*', ha='center', va='center', fontsize=20, color='red')

plt.title("2D Grid World with Optimal Policy")
plt.show()