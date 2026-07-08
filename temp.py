import numpy as np
# ==================== 4x4 GridWorld Environment ====================
SIZE = 4
N_STATES = SIZE * SIZE          # Total 16 states (0 to 15)
TERMINALS = {0, 15}             # Top-left and bottom-right are terminals
ACTIONS = [0, 1, 2, 3]          # 0 = Up, 1 = Right, 2 = Down, 3 = Left


def is_terminal(state):
    """Check if the state is a terminal state"""
    return state in TERMINALS


def get_next_state(state, action):
    """Find the next state after taking an action"""
    if is_terminal(state):
        return state
    
    # Convert state number to row and column
    row = state // SIZE
    col = state % SIZE
    
    # Move according to action
    if action == 0:      # Up
        row = max(0, row - 1)
    elif action == 1:    # Right
        col = min(SIZE - 1, col + 1)
    elif action == 2:    # Down
        row = min(SIZE - 1, row + 1)
    elif action == 3:    # Left
        col = max(0, col - 1)
    
    # Convert row, col back to state number
    return row * SIZE + col


def take_action(state, action):
    """Take one step in the environment. Returns (next_state, reward)"""
    if is_terminal(state):
        return state, 0
    
    next_state = get_next_state(state, action)
    reward = -1          # -1 reward for every step (encourages reaching terminal faster)
    return next_state, reward


# ==================== Policy Evaluation ====================

def policy_evaluation(policy, gamma=0.9, theta=0.0001):
    """
    Evaluate how good the given policy is.
    Uses synchronous updates (safer and easier to understand).
    """
    # Start with all values as 0
    V = np.zeros(N_STATES)
    iteration = 0
    
    while True:
        delta = 0                           # Track biggest change in this iteration
        V_new = np.copy(V)                  # We update in a new array (synchronous)
        
        for s in range(N_STATES):
            if is_terminal(s):
                V_new[s] = 0
                continue
            
            v = 0.0                         # Expected value for this state
            
            # Go through all 4 actions
            for a_idx, action in enumerate(ACTIONS):
                prob = policy[s, a_idx]     # Probability of taking this action
                if prob == 0:
                    continue
                
                next_s, reward = take_action(s, action)
                v += prob * (reward + gamma * V[next_s])
            
            V_new[s] = v
            delta = max(delta, abs(V_new[s] - V[s]))
        
        V = V_new
        iteration += 1
        
        # Stop when values stop changing much
        if delta < theta:
            break
    
    return V, iteration


# ==================== Run Policy Evaluation ====================

# Create a random policy (25% chance for each action)
# Terminals have no actions (all probabilities = 0)
policy = np.ones((N_STATES, 4)) / 4.0
for t in TERMINALS:
    policy[t] = 0

print("Running Policy Evaluation...")
print("Policy: Random (equal probability for all 4 actions)\n")

V, iterations = policy_evaluation(policy, gamma=0.9, theta=1e-4)

print(f"Converged in {iterations} iterations\n")
print("Final Value Function (4x4 grid):")
print(np.round(V.reshape(SIZE, SIZE), 2))