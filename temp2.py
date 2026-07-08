import numpy as np
# ==================== Line World Environment ====================
# States arranged in a line:
#   T0  --  A  --  B  --  T1
# T0 and T1 are terminals.
# From A: Left goes to T0, Right goes to B
# From B: Left goes to A, Right goes to T1
# Reward = -1 every step
TERMINALS = {0, 3}

def is_terminal(state):
    """Check if the state is terminal"""
    return state in TERMINALS


def get_next_state(state, action):
    """Return next state after taking an action (0=Left, 1=Right)"""
    if is_terminal(state):
        return state
    
    if state == 1:                    # State A
        if action == 0:               # Left
            return 0                  # Go to T0
        else:                         # Right
            return 2                  # Go to B
    
    elif state == 2:                  # State B
        if action == 0:               # Left
            return 1                  # Go to A
        else:                         # Right
            return 3                  # Go to T1
    
    return state


def take_step(state, action):
    """Take one step in the environment"""
    if is_terminal(state):
        return state, 0
    
    next_state = get_next_state(state, action)
    reward = -1
    return next_state, reward

def policy_evaluation(gamma=0.9, theta=0.0001):
    # Start with value = 0 for all 4 states
    V = np.zeros(4)
    iteration = 0
    
    while True:
        delta = 0
        V_new = np.copy(V)   
        v = 0.0
        # Action Left with probability 0.5
        next_s, r = take_step(1, 0)
        v += 0.5 * (r + gamma * V[next_s])
        
        # Action Right with probability 0.5
        next_s, r = take_step(1, 1)
        v += 0.5 * (r + gamma * V[next_s])
        
        V_new[1] = v
        delta = max(delta, abs(V_new[1] - V[1]))
        
        # --- Update state B (index 2) ---
        v = 0.0
        # Action Left with probability 0.5
        next_s, r = take_step(2, 0)
        v += 0.5 * (r + gamma * V[next_s])
        
        # Action Right with probability 0.5
        next_s, r = take_step(2, 1)
        v += 0.5 * (r + gamma * V[next_s])
        
        V_new[2] = v
        delta = max(delta, abs(V_new[2] - V[2]))
        
        # Terminals are always 0
        V_new[0] = 0
        V_new[3] = 0
        
        V = V_new
        iteration += 1
        
        if delta < theta:
            break
    
    return V, iteration
print("Line World - Policy Evaluation")
print("States: T0(0) -- A(1) -- B(2) -- T1(3)")
print("Policy: Random (50% Left, 50% Right)\n")

V, iterations = policy_evaluation(gamma=0.9, theta=1e-4)

print(f"Converged in {iterations} iterations\n")
print("Final Value Function:")
print(f"  T0 (0): {V[0]:.2f}")
print(f"   A (1): {V[1]:.2f}")
print(f"   B (2): {V[2]:.2f}")
print(f"  T1 (3): {V[3]:.2f}")