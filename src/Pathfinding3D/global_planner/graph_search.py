"""
@file: graph_search.py
@breif: Base class for planner based on graph searching
@author: Winter
@update: 2023.1.13
"""
import math

import numpy as np

# from python_motion_planning.utils import Env, Node, Planner, Grid

from src.Pathfinding3D.environment3D.env import Env, Grid
from src.Pathfinding3D.utils.planner.planner import Planner
from src.Pathfinding3D.environment3D.node import Node
class GraphSearcher(Planner):
    """
    Base class for planner based on graph searching.

    Parameters:
        start (tuple): start point coordinate
        goal (tuple): goal point coordinate
        env (Grid): environment
        heuristic_type (str): heuristic function type
    """
    def __init__(self, start: tuple, goal: tuple, env: Grid, heuristic_type: str="euclidean") -> None:
        super().__init__(start, goal, env)
        # heuristic type
        self.heuristic_type = heuristic_type
        # allowed motions
        self.motions = self.env.motions
        # obstacles
        self.obstacles = self.env.obstacles

    def h(self, node: Node, goal: Node) -> float:
        """
        Calculate heuristic.

        Parameters:
            node (Node): current node
            goal (Node): goal node

        Returns:
            h (float): heuristic function value of node
        """
        if self.heuristic_type == "manhattan":
            return abs(goal.x - node.x) + abs(goal.y - node.y) + abs(goal.z - node.z)
        elif self.heuristic_type == "euclidean":
            return math.hypot(goal.x - node.x, goal.y - node.y, goal.z - node.z)

    def cost(self, node1: Node, node2: Node) -> float:
        """
        Calculate cost for this motion.

        Parameters:
            node1 (Node): node 1
            node2 (Node): node 2

        Returns:
            cost (float): cost of this motion
        """
        if self.isCollision(node1, node2):
            return float("inf")
        return self.dist(node1, node2)

    def isCollision(self, node1: Node, node2: Node) -> bool:
        """
        Judge collision when moving from node1 to node2.

        Parameters:
            node1 (Node): node 1
            node2 (Node): node 2

        Returns:
            collision (bool): True if collision exists else False
        """
        # check if current node or next is an obstacle
        if node1.current in self.obstacles or node2.current in self.obstacles:
            return True

        x1, y1, z1 = node1.x, node1.y, node1.z
        x2, y2, z2 = node2.x, node2.y, node2.z

        # how did we move along each axis for this step
        dx, dy, dz = x2 - x1, y2 - y1, z2 - z1

        # calculate how many axes changed (0, 1, 2, or 3)
        k = np.count_nonzero([dx, dy, dz])

        # moving along 0 or 1 axis only (straight move only)
        if k <= 1:
            return False

        # direction of steps on each axis: +1 (increase), -1 (decrease), or 0 (no move)
        if dx > 0:
            sx = 1
        elif dx < 0:
            sx = -1
        else:
            sx = 0

        if dy > 0:
            sy = 1
        elif dy < 0:
            sy = -1
        else:
            sy = 0

        if dz > 0:
            sz = 1
        elif dz < 0:
            sz = -1
        else:
            sz = 0

        # for diagonal moves (k = 2 or 3), check the face-adjacent cells next to the current node to prevent corner-cutting
        # check x neighbor
        if sx and (x1 + sx, y1, z1) in self.obstacles:
            return True  # collision detected

        # check y neighbor
        if sy and (x1, y1 + sy, z1) in self.obstacles:
            return True  # collision detected

        # check z neighbor
        if sz and (x1, y1, z1 + sz) in self.obstacles:
            return True  # collision detected

        # none of the side cells are obstacles
        return False  # no collision so safe to move

        #if x1 != x2 and y1 != y2 and z1 != z2:
            #if x2 - x1 == y1 - y2:
                #s1 = (min(x1, x2), min(y1, y2), z1)
                #s2 = (max(x1, x2), max(y1, y2), z2)
            #else:
                #s1 = (min(x1, x2), max(y1, y2), z1)
                #s2 = (max(x1, x2), min(y1, y2), z2)
            #if s1 in self.obstacles or s2 in self.obstacles:
                #return True
        # 2D diagonal in XY plane
        #elif x1 != x2 and y1 != y2:
            #if x2 - x1 == y1 - y2:
                #s1 = (min(x1, x2), min(y1, y2), z1)
                #s2 = (max(x1, x2), max(y1, y2), z1)
            #else:
                #s1 = (min(x1, x2), max(y1, y2), z1)
                #s2 = (max(x1, x2), min(y1, y2), z1)
            #if s1 in self.obstacles or s2 in self.obstacles:
                #return True
        #return False

