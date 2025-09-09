# 3D Pathfinding Example with your updated files
#import python_motion_planning as pmp
import numpy as np
import matplotlib.pyplot as plt
from fontTools.misc.py23 import xrange

from src.Pathfinding3D.environment3D.env import Grid, Env
from src.Pathfinding3D.global_planner.a_star import AStar
from src.Pathfinding3D.global_planner.dijkstra import Dijkstra
from src.Pathfinding3D.global_planner.jps import JPS
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

    if z1 is None:
        z1 = nz - 1 # default to last z-index
    x0, y0 = 0, 0

    # along X from x0 to nx-1 at fixed y in [y0 .. y0+thickness-1]
    for x in range(x0, nx):
        for y in range(y0, min(y0 + thickness, ny)):
            for z in range(z0, z1 + 1):
                obstacles.add((x, y, z))

    # along Y from y0 to ny-1 at fixed x in [x0 .. x0+thickness-1]
    for y in range(y0, ny):
        for x in range(x0, min(x0 + thickness, nx)):
            for z in range(z0, z1 + 1):
                obstacles.add((x, y, z))




# Build corner wall using ~40% of grid span in X and Y
add_corner_wall(obstacles, env, z0=0, z1=env.z_range - 1, thickness=1)

# adding random buildings obstacles
for z in range(10):
    obstacles.add((18, 17, z))

for z in range(9):
    obstacles.add((4, 4, z))

for z in range(10):
    obstacles.add((9, 8, z))

for z in range(10):
    obstacles.add((15, 10, z))

for z in range(10):
    obstacles.add((18, 4, z))

for z in range(10):
    obstacles.add((5, 16, z))

for z in range(10):
    obstacles.add((24, 12, z))

for z in range(10):
    obstacles.add((5, 16, z))

for z in range(10):
    obstacles.add((12, 16, z))

for z in range(10):
    obstacles.add((24, 18, z))


# Update env with new obstacles
env.update(obstacles)

# A* algorithm
planner = AStar(start=(2, 2, 7), goal=(18, 17, 10), env=env)
cost, path, expand = planner.plan()
planner.plot.ax.view_init(elev=30, azim=80) # rotating plot angle
planner.plot.animation(path, str(planner), cost, expand=None)

# Dijkstra algorithm
planner2 = Dijkstra(start=(2, 2, 7), goal=(18, 17, 10), env=env)
cost2, path2, expand2 = planner2.plan()
planner2.plot.ax.view_init(elev=30, azim=80) # rotating plot angle
planner2.plot.animation(path2, str(planner2), cost2, expand=None)

# JPS algorithm
planner3 = JPS(start=(2, 2, 7), goal=(18, 17, 10), env=env)
cost3, path3, exapnd3 = planner3.plan()
planner3.plot.ax.view_init(elev=30, azim=80)
planner3.plot.animation(path3, str(planner3), cost3, expand=None)
