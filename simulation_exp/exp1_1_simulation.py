import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.map_to_robot_simulation import Simulation
import time

env = Simulation()

env.map_to_robot('exp1_1_1', 10)
time.sleep(2)

env.map_to_robot('exp1_1_2', 5)