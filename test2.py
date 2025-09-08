# 3D Pathfinding Example with your updated files
#import python_motion_planning as pmp
import numpy as np
import matplotlib.pyplot as plt
#import environment3D
from src.Pathfinding3D.environment3D.env import Grid, Env
from src.Pathfinding3D.global_planner.a_star import AStar
from src.Pathfinding3D.global_planner.dijkstra import Dijkstra
from src.Pathfinding3D.utils.plot.plot import Plot
from src.Pathfinding3D.utils.agent.agent import Robot
from src.Pathfinding3D.environment3D.node import Node
from src.Pathfinding3D.utils.planner.planner import Planner

# Create environment with custom obstacles
env = Grid(50, 35, 10)
obstacles = set()

# create obstacles
for i in range(10, 21):
    obstacles.add((i, 15, 0))

for i in range(15):
    obstacles.add((20, i, 8))

for i in range(15, 30):
    obstacles.add((30, i, 10))

for i in range(16):
    obstacles.add((40, i, 3))

for z in range(10):
    obstacles.add((25, 15, z))


# Update env with new obstacles
env.update(obstacles)

# A* algorithm
planner = AStar(start=(5, 5, 10), goal=(45, 25, 0), env=env)
cost, path, expand = planner.plan()
planner.plot.ax.view_init(elev=50, azim=45) # rotating plot angle
planner.plot.animation(path, str(planner), cost, expand=None)

# Dijkstra algorithm
planner2 = Dijkstra(start=(5, 5, 10), goal=(45, 25, 0), env=env)
cost2, path2, expand2 = planner2.plan()
planner2.plot.ax.view_init(elev=50, azim=45) # rotating plot angle
planner2.plot.animation(path2, str(planner2), cost2, expand=None)
