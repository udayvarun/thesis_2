import panda_py
import numpy as np
from panda_py import libfranka
from panda_py import constants
from panda_py import controllers

import roboticstoolbox as rtb
import spatialmath as sm

class Panda:
    def __init__(self):
        self.hostname = "192.168.1.101" 
    
        desk = panda_py.Desk(self.hostname, "asm_panda" , "asmpanda123" )
        desk.unlock()
        desk.activate_fci()
        self.panda = panda_py.Panda(self.hostname)
        
        self.stiffness = np.array([600., 600., 600., 600., 250., 150., 50.])
        self.damping = np.array([50., 50., 50., 20., 20., 20., 10.])
    
        self.stiffness = self.stiffness * 0.2 * 5
        self.damping = self.damping * 0.4
        
        # Initialize roboticstoolbox model
        self.panda_rtb = rtb.models.Panda()
        
    def get_robot_position(self):
        return self.panda.get_state().q
    
    def forward_kinematics(self, q):
        return self.panda_rtb.fkine(q)
    
    def robot_mapper(self, runtime):
        self.panda.move_to_start()
        ctrl = controllers.JointPosition()
    
        self.panda.start_controller(ctrl)
    
        start_position = self.get_robot_position()
        print("Start Position:\n",start_position)
        cartesian_start_position = self.forward_kinematics(start_position)
        print("Cartesian Start Position:\n",cartesian_start_position)
    
        print("Stifness:\n", self.stiffness)
    
        ctrl.set_stiffness(self.stiffness)
        ctrl.set_damping(self.damping)

        print(self.forward_kinematics(self.panda.q))
        with self.panda.create_context(frequency=1e2, max_runtime=runtime) as ctx:
            while ctx.ok():
                qd = start_position.copy()
                qd[0] += 0.4 * np.sin(ctrl.get_time())
                ctrl.set_control(qd)


