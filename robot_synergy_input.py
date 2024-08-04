import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

# Define the cost function
def cost_function(u):
    q = np.zeros((T+1, nq))
    u = u.reshape((T, nu))
    q[0] = q0
    cost = 0
    
    ## System function
    # Lagrange term
    for t in range(T):
        q[t+1] = q[t] + np.matmul(S, u[t]) #*dt
        if t < T-1:
            # Costs for change in u
            cost += np.sum(2.0*(u[t+1] - u[t])**2)
    
    # Mayer term
    # Costs for deviation to goal position (Here: joint positions)
    cost += np.sum( (q[-1] - q_goal)**2 ) 
    return cost

# Define the constraint that the last control input must be zero (start with zero velocity)
def end_control_constraint(u):
    u = u.reshape(T, nu)
    return u[-1]

# Define the constraint that the last control input must be zero (stop with zero velocity)
def start_control_constraint(u):
    u = u.reshape(T, nu)
    return u[0]


## Parameters
T = 100  # Steps in time horizon
nu = 3 # Number of PCA components used
nq = 7 # Number of robot joints

# Initial joint position
q0 = np.array([1.0, 0.5, 0.6, 0.4, 0.3, 0.1, 0.0])  

# Synergy matrix: Contains PCA components
S = np.array([[1.0,1.0,1.0,1.0,1.0,1.0,1.0,],[0.1,0.2,0.3,0.4,0.5,0.6,0.7],[-0.5,0.5,-0.5,-0.5,-0.5,-0.5,-0.5]])
S = np.transpose(S)

# Initial guess for the control inputs
u_initial = np.zeros((T, nu))

# Desired goal position in joint space
q_goal = np.array([0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1])


## Constraints (first and last control input should be zero, rate of change constraint)
constraints = [
    {'type': 'eq', 'fun': start_control_constraint},
    {'type': 'eq', 'fun': end_control_constraint}
]


## Optimize
result = minimize(cost_function, u_initial, constraints=constraints)

# Optimal control inputs and states (recreate the joint trajectories)
u_optimal = result.x.reshape(T, nu)
q_optimal = np.zeros((T+1, nq))
q_optimal[0] = q0
for t in range(T):
    q_optimal[t+1] = q_optimal[t] + np.matmul(S, u_optimal[t])


## Plot the results
time = np.arange(T+1)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15, 10))

# Plot für die Zustandsvariablen
for i in range(q_optimal.shape[1]):
    ax1.plot(time, q_optimal[:, i], label=f'State {i+1}')
    ax1.set_xlabel('Time')
    ax1.set_ylabel('State Variables')
    ax1.legend()
    ax1.grid(True)
    ax1.set_title('State Variables over Time')

# Plot für die Steuerungsvariablen
for i in range(nu):
    if nu > 1:
        ax2.plot(time[:-1], u_optimal[:, i], label=f'Control {i+1}')
    else:
        ax2.plot(time[:-1], u_optimal, label=f'Control {i+1}')
    ax2.set_xlabel('Time')
    ax2.set_ylabel('Control Variables')
    ax2.legend()
    ax2.grid(True)
    ax2.set_title('Control Variables over Time')

plt.tight_layout()
plt.show()

