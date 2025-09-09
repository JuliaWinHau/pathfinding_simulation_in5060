# 3D Pathfinding Example with your updated files
#import python_motion_planning as pmp
import numpy as np
import matplotlib.pyplot as plt
import random
from fontTools.misc.py23 import xrange

from src.Pathfinding3D.environment3D.env import Grid, Env
from src.Pathfinding3D.global_planner.a_star import AStar
from src.Pathfinding3D.global_planner.dijkstra import Dijkstra
from src.Pathfinding3D.global_planner.jps import JPS
from src.Pathfinding3D.global_planner.lazy_theta_star import LazyThetaStar
from src.Pathfinding3D.global_planner.gbfs import GBFS
# from src.Pathfinding3D.utils.plot.plot import Plot
# from src.Pathfinding3D.utils.agent.agent import Robot
# from src.Pathfinding3D.environment3D.node import Node
# from src.Pathfinding3D.utils.planner.planner import Planner

# Create environment with custom obstacles
env = Grid(25, 20, 12)
obstacles = set()

def add_corner_wall(obstacles, env, z0=0, z1=None, thickness=1):
    """
    Corner wall boundary runs the full length of both sides.
    - corner: (x0, y0) where the two walls meet (e.g., (0,0) for lower-left corner)
    - thickness: how many voxels thick to make each wall (prevents diagonal slips)
    """
    nx, ny, nz = env.x_range, env.y_range, env.z_range # get grid size (x, y, z)

    # if no explicit top height given, use the top layer (last valid z index)
    if z1 is None:
        z1 = nz - 1  # default to last z-index

    x0, y0 = 0, 0  # corner where the two walls meet

    # min(y0 + thickness, ny) clips the stripe so we never exceed the grid height ny
    for x in range(x0, nx):  # span full X: 0..nx-1
        for y in range(y0, min(y0 + thickness, ny)):  # to build a wall Y near y0
            for z in range(z0, z1 + 1):  # # vertical extent from z0 to z1
                obstacles.add((x, y, z))

    # min(x0 + thickness, nx) clips the stripe so we never exceed the grid width nx
    for y in range(y0, ny):  # span full Y: 0..ny-1
        for x in range(x0, min(x0 + thickness, nx)):  # to build a wall X near x0
            for z in range(z0, z1 + 1):  # vertical extent from z0 to z1
                obstacles.add((x, y, z))



# Build corner wall
add_corner_wall(obstacles, env, z0=0, z1=env.z_range - 1, thickness=1)

# adding random buildings obstacles
def generate_obstacles(amount=30, x_max=25, y_max=20, z_max=12):
    random.seed(5)
    for _ in range(amount):
        x = random.randrange(x_max)
        y = random.randrange(y_max)
        height = random.randrange(5, z_max)
        for z in range(height):
            obstacles.add((x, y, z))
    
generate_obstacles()

# Update env with new obstacles
env.update(obstacles)

#### Test different algorithms ####
# A* algorithm
planner = AStar(start=(1, 1, 0), goal=(18, 17, 10), env=env)
cost, path, expand = planner.plan()
planner.plot.ax.view_init(elev=30, azim=80) # rotating plot angle
planner.plot.animation(path, str(planner), cost, expand=None)

# Dijkstra algorithm
planner2 = Dijkstra(start=(1, 1, 0), goal=(18, 17, 10), env=env)
cost2, path2, expand2 = planner2.plan()
planner2.plot.ax.view_init(elev=30, azim=80) # rotating plot angle
planner2.plot.animation(path2, str(planner2), cost2, expand=None)

# JPS algorithm
planner3 = JPS(start=(1, 1, 0), goal=(18, 17, 10), env=env)
cost3, path3, exapnd3 = planner3.plan()
planner3.plot.ax.view_init(elev=30, azim=80)
planner3.plot.animation(path3, str(planner3), cost3, expand=None)

# Lazy Theta* algorithm
planner4 = LazyThetaStar(start=(1, 1, 0), goal=(18, 17, 10), env=env)
cost4, path4, exapnd4 = planner4.plan()
planner4.plot.ax.view_init(elev=30, azim=80)
planner4.plot.animation(path4, str(planner4), cost4, expand=None)

planner5 = GBFS(start=(1, 1, 0), goal=(18, 17, 10), env=env)
cost5, path5, exapnd5 = planner5.plan()
planner5.plot.ax.view_init(elev=30, azim=80)
planner5.plot.animation(path5, str(planner5), cost5, expand=None)