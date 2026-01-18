# Grid World Reinforcement Learning Experiments

This repository contains two Python implementations for solving a **Grid World navigation problem** using classical **Reinforcement Learning (RL)** techniques:

1. **Value Iteration (Dynamic Programming)**
2. **Q-Learning (Model-Free Reinforcement Learning)**

Both implementations allow interactive user input, compute an optimal policy, and visualize the resulting policy using **Matplotlib**.

---

## 1. Value Iteration (Question 1)

### Description

This program implements the **Value Iteration algorithm**, a model-based dynamic programming method for solving Markov Decision Processes (MDPs).

The agent navigates a 2D grid world and learns the optimal state-value function. From this value function, the optimal policy is derived.

### Key Features

* User-defined grid size (e.g., 5×5)
* User-defined goal location
* Deterministic actions: Up, Down, Left, Right
* Reward structure:

  * **+10** for reaching the goal
  * **-1** for each step or invalid move
* Discount factor ( \gamma = 0.9 )
* Convergence threshold for value iteration
* Console output of the optimal policy
* 2D visualization of the grid with policy arrows

### Algorithm Overview

1. Initialize the value function ( V(s) = 0 ) for all states
2. Iteratively update values using the Bellman optimality equation
3. Stop when value updates converge
4. Extract the optimal policy from the converged value function
5. Visualize the policy

### Policy Symbols

* `^` : Move Up
* `v` : Move Down
* `<` : Move Left
* `>` : Move Right
* `*` : Goal state

---

## 2. Q-Learning (Question 2)

### Description

This program implements **Q-Learning**, a model-free reinforcement learning algorithm. The agent learns action-values through interaction with the environment using an **epsilon-greedy exploration strategy**.

### Key Features

* User-defined grid size and goal location
* No prior knowledge of transition dynamics
* Epsilon-greedy exploration
* Random initial starting position per episode
* Reward structure:

  * **+10** for reaching the goal
  * **-1** for each step
* Console output of learned Q-values
* Derived optimal policy from the Q-table
* 2D visualization of the learned policy

### Hyperparameters

* Learning rate ( \alpha = 0.5 )
* Discount factor ( \gamma = 0.9 )
* Exploration rate ( \epsilon = 0.1 )
* Number of episodes: 1000

### Algorithm Overview

1. Initialize Q-values to zero
2. For each episode:

   * Start from a random state
   * Select actions using epsilon-greedy policy
   * Update Q-values using the Q-learning update rule
3. After training, derive the optimal policy
4. Visualize the policy

---

## Visualization

Both programs generate a **2D grid visualization**:

* Each cell displays the optimal action as an arrow
* The goal state is marked with a red `*`
* Grid lines clearly show state boundaries

---

## Requirements

Make sure the following packages are installed:

* Python 3.x
* NumPy
* Matplotlib

Install dependencies using:

```bash
pip install numpy matplotlib
```

---

## How to Run

1. Run the desired Python file:

```bash
python value_iteration.py
```

or

```bash
python q_learning.py
```

2. Enter:

   * Grid size (e.g., `5` for a 5×5 grid)
   * Goal row index
   * Goal column index

3. View:

   * Optimal policy printed in the terminal
   * Graphical visualization window

---

## Learning Outcomes

* Understand the difference between **model-based** and **model-free** RL
* Visualize optimal policies in grid environments
* Compare Value Iteration vs Q-Learning behavior
* Gain intuition about rewards, discounting, and exploration

---

## Notes

* Value Iteration assumes full knowledge of the environment
* Q-Learning learns purely from experience
* Due to randomness, Q-Learning results may slightly vary between runs

---

## Author

Developed as part of a Reinforcement Learning assignment.

---

Feel free to extend this project with obstacles, stochastic transitions, or multiple goals.
