# Human-likeness of robot arm motion with postural synergies

This page is under construction

## Dependances

- [Robotics toolbox python](https://github.com/petercorke/robotics-toolbox-python.git)
  - If using windows current version 1.1.0 needs two fixes to run the current code
    - Graphical visualsaion via swift is currently not supported under Windows. However there is a hotfix, by changing in ```SwiftRoute.py``` ```self.path[9:]``` to  ```self.path[10:]``` [More info](https://github.com/petercorke/robotics-toolbox-python/pull/402)
    - There was one place where from scipy import randn was called: the roboticstoolbox/mobile/EKF.py but it was not used and causing error. [More info](https://github.com/petercorke/robotics-toolbox-python/pull/413)

## Description of the code

- Run the main.py and it will extract the joint angles from the data set and do pca and can see it on the graph.
- Then it opens swift and loops the desired motion until the program is stopped.
