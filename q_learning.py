""" Enhanced Implementation of Q-Learning Algorithm for Question 2
This version allows user input for grid size and goal position.
It performs Q-learning with epsilon-greedy exploration.
After training, it prints the learned Q-values for each state.
Additionally, it derives the optimal policy from the Q-table and prints it.
Finally, it uses matplotlib to plot a 2D visualization of the grid world with policy arrows.
Arrows indicate the optimal action: ^ (up), v (down), < (left), > (right), * (goal).
Run this code in a Python environment with matplotlib installed to see the plot.
"""
import random 
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

alpha = 0.5 
gamma = 0.9 
epsilon = 0.1 
num_episodes = 1000 

# Initialize Q-table as grid_size x grid_size x 4 list of 0.0
Q = [[[0.0 for _ in range(4)] for _ in range(grid_size)] for _ in range(grid_size)]

# Q-learning training
for episode in range(num_episodes): 

    i = random.randint(0, grid_size - 1)
    j = random.randint(0, grid_size - 1)
    while (i, j) != goal: 
        if random.random() < epsilon:
            a = random.randint(0, 3)
        else:  
            a = max(range(4), key=lambda x: Q[i][j][x])  
        ni = i + actions[a][0] 
        nj = j + actions[a][1]
        if not (0 <= ni < grid_size and 0 <= nj < grid_size):
            ni, nj = i, j
        r = 10 if (ni, nj) == goal else -1 

        best_next_q = max(Q[ni][nj])
        Q[i][j][a] += alpha * (r + gamma * best_next_q - Q[i][j][a])
        i, j = ni, nj

# Print learned Q-values
print("\nLearned Q-values:")
for i in range(grid_size):
    for j in range(grid_size):
        print(f"State ({i}, {j}): {[round(q, 2) for q in Q[i][j]]}") 

# Derive optimal policy from Q-table
policy = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]
policy_arrows = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]
for i in range(grid_size):
    for j in range(grid_size):
        if (i, j) == goal:
            policy[i][j] = 'G'
            policy_arrows[i][j] = '*'
            continue
        best_a = max(range(4), key=lambda x: Q[i][j][x])
        policy[i][j] = action_symbols[best_a]
        policy_arrows[i][j] = action_arrows[best_a]

# Print the optimal policy from Q learning
print("\nDerived Optimal Policy:")
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

plt.title("2D Grid World with Derived Optimal Policy from Q-Learning")  # Title.
plt.show()