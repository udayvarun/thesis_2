import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

class minimize_dataset:
    def __init__(self, S):
        # Synergy matrix: Contains PCA components
        self.S = np.transpose(S)
        ## Parameters
        self.T = 100  # Steps in time horizon
        self.nu = 7 # Number of PCA components used
        self.nq = 7 # Number of robot joints
        # Initial joint position
        self.q0 = np.array([1.0, 0.5, 0.6, 0.4, 0.3, 0.1, 0.0])  
        # Desired goal position in joint space
        self.q_goal = np.array([0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1])
    
    # Define the cost function
    def cost_function(self, u):
        q = np.zeros((self.T+1, self.nq))
        u = u.reshape((self.T, self.nu))
        q[0] = self.q0
        cost = 0
        
        ## System function
        # Lagrange term
        for t in range(self.T):
            q[t+1] = q[t] + np.matmul(self.S, u[t]) #*dt
            if t < self.T-1:
                # Costs for change in u
                cost += np.sum(2.0*(u[t+1] - u[t])**2)
        
        # Mayer term
        # Costs for deviation to goal position (Here: joint positions)
        cost += np.sum( (q[-1] - self.q_goal)**2 ) 
        return cost

    # Define the constraint that the last control input must be zero (start with zero velocity)
    def end_control_constraint(self, u):
        u = u.reshape(self.T, self.nu)
        return u[-1]

    # Define the constraint that the last control input must be zero (stop with zero velocity)
    def start_control_constraint(self, u):
        u = u.reshape(self.T, self.nu)
        return u[0]

    def minimize_function(self, intial_position = None, goal_position = None ):
        if intial_position is not None:
            self.q0 = intial_position
        if goal_position is not None:
            self.q_goal = goal_position
        # Initial guess for the control inputs
        self.u_initial = np.zeros((self.T, self.nu))

        ## Constraints (first and last control input should be zero, rate of change constraint)
        self.constraints = [
            {'type': 'eq', 'fun': self.start_control_constraint},
            {'type': 'eq', 'fun': self.end_control_constraint}
        ]

        ## Optimize
        result = minimize(self.cost_function, self.u_initial, constraints=self.constraints)

        # Optimal control inputs and states (recreate the joint trajectories)
        self.u_optimal = result.x.reshape(self.T, self.nu)
        self.q_optimal = np.zeros((self.T+1, self.nq))
        self.q_optimal[0] = self.q0
        for t in range(self.T):
            self.q_optimal[t+1] = self.q_optimal[t] + np.matmul(self.S, self.u_optimal[t])

        return self.q_optimal
    
    def plot_variables(self):
        time = np.arange(self.T+1)
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15, 10))

        # Plot für die Zustandsvariablen
        for i in range(self.q_optimal.shape[1]):
            ax1.plot(time, self.q_optimal[:, i], label=f'State {i+1}')
            ax1.set_xlabel('Time')
            ax1.set_ylabel('State Variables')
            ax1.legend()
            ax1.grid(True)
            ax1.set_title('State Variables over Time')

        # Plot für die Steuerungsvariablen
        for i in range(self.nu):
            if self.nu > 1:
                ax2.plot(time[:-1], self.u_optimal[:, i], label=f'Control {i+1}')
            else:
                ax2.plot(time[:-1], self.u_optimal, label=f'Control {i+1}')
            ax2.set_xlabel('Time')
            ax2.set_ylabel('Control Variables')
            ax2.legend()
            ax2.grid(True)
            ax2.set_title('Control Variables over Time')

        plt.tight_layout()
        plt.show()
