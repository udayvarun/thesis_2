# Human-likeness of robot arm motion with postural synergies

## Dependances

- [Robotics toolbox python](https://github.com/petercorke/robotics-toolbox-python.git)
  - If using windows current version 1.1.0 needs two fixes to run the current code
    - Graphical visualsaion via swift is currently not supported under Windows. However there is a hotfix, by changing in ```SwiftRoute.py``` ```self.path[9:]``` to  ```self.path[10:]``` [More info](https://github.com/petercorke/robotics-toolbox-python/pull/402)
    - There was one place where from scipy import randn was called: the roboticstoolbox/mobile/EKF.py but it was not used and causing error. [More info](https://github.com/petercorke/robotics-toolbox-python/pull/413)

## Folder Structure

Here is the folder structure of the project with comments

```markdown
.
├── data_sets # experiments of the dataset 
├── experiment_data_set # generated trajectories for experiments
├── questionnaire # questionnarie documents, graphs, results
├── real_robot_example # panda_py examples
├── simulation_exp # simulation execution files
├── utils # all supported files
├── exp_end.py # get back to default start position of panda robot
├── exp_start.py # get to the initial position of the experiments
├── exp0.py # expeiment template
├── exp1_1.py
├── exp1_2.py
├── exp1_3.py
├── exp2_1.py
├── exp2_2.py
├── exp2_3.py
├── exp3_1.py
├── exp3_2.py
├── exp3_3.py
└── README.md
```

## Running the experiments

- Run the `exp_start.py` to get to the start position of the robot arm.
- Run the files `exp*_*.py` on the root folder to run the experiment on the robot.
- Check the credentials in the `real_robot_mapper.py` to match the robot currently used.
- The experiment trajectories are already generated. Uncomment the lines in the code to generate the files again (`utils\calculate_q.py` will generate the trajectories).
- Use `exp0.py` as template for more experiments.
- Run the `exp_end.py` to get to back to the original start position of the robot arm.
- Run the files in the `.\simulation_exp` to start simulation experiments.
