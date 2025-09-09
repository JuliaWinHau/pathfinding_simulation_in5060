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

def add_floor(obstacles, env, z0=0, thickness=1):
    """
    Add a horizontal obstacle floor spanning the full X and Y dimensions.
    - z0: starting height of the floor
    - thickness: how many layers thick the floor should be
    """
    nx, ny, nz = env.x_range, env.y_range, env.z_range

    # floor spans all x and y, but only thickness layers in z
    for x in range(nx):
        for y in range(ny):
            for z in range(z0, min(z0 + thickness, nz)):
                obstacles.add((x, y, z))

# Build corner wall
# add_corner_wall(obstacles, env, z0=0, z1=env.z_range - 1, thickness=1)
add_floor(obstacles, env, z0=0, thickness=1)

# adding random buildings obstacles
random.seed(5)
def generate_obstacles(obstacle_amount=20, x_max=25, y_max=20, z_max=12):
    for _ in range(obstacle_amount):
        x = random.randrange(x_max)
        y = random.randrange(y_max)
        height = random.randrange(5, z_max)
        for z in range(height):
            obstacles.add((x, y, z))

def generate_obstacle_gridlike(obstacle_amount=20, x_max=25, y_max=20, z_max=12):
    for x in range(0, 25, 7):
        for y in range(0, 20, 4):
            for z in range(10):
                for i in range(4):                    
                    obstacles.add((x + i, y, z))
                

# generate_obstacles(obstacle_amount=100)
generate_obstacle_gridlike()

# Update env with new obstacles
env.update(obstacles)

#### Test different algorithms ####
start_position = (1, 1, 11)
goal_position = (18, 20, 1)
costs = []

def simulate_algorithm(algorithm):
    planner = algorithm
    cost, path, expand = planner.plan()
    planner.plot.ax.view_init(elev=50, azim=80) # rotating plot angle
    planner.plot.animation(path, str(planner), cost, expand=None)
    costs.append(cost)

simulate_algorithm(AStar(start_position, goal=goal_position, env=env))
# simulate_algorithm(Dijkstra(start_position, goal=(goal_position), env=env))
# simulate_algorithm(JPS(start_position, goal=(goal_position), env=env))
simulate_algorithm(LazyThetaStar(start_position, goal=(goal_position), env=env))
simulate_algorithm(GBFS(start_position, goal=(goal_position), env=env))

algorithms = ["A*", "LazyThetaStar", "GBFS"]
plt.bar(algorithms, costs, color="skyblue", edgecolor="black")
plt.ylabel("Cost")
plt.title("Cost Comparison")

# Add labels above bars
for i, cost in enumerate(costs):
    plt.text(i, cost + 0.5, str(cost), ha='center', va='bottom')

plt.show()



