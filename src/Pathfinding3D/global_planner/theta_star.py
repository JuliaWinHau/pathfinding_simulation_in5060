"""
@file: theta_star.py
@breif: Theta* motion planning
@author: Yang Haodong, Wu Maojia
@update: 2024.6.23
"""
import heapq

from .a_star import AStar
from src.Pathfinding3D.environment3D.env import Grid, Env
from src.Pathfinding3D.environment3D.node import Node
from src.Pathfinding3D.global_planner .a_star import AStar
# from python_motion_planning.utils import Env, Node, Grid


class ThetaStar(AStar):
    """
    Class for Theta* motion planning.

    Parameters:
        start (tuple):
            start point coordinate
        goal (tuple):
            goal point coordinate
        env (Grid):
            environment
        heuristic_type (str):
            heuristic function type

    Examples:
        >>> import python_motion_planning as pmp
        >>> planner = pmp.ThetaStar((5, 5), (45, 25), pmp.Grid(51, 31))
        >>> cost, path, expand = planner.plan()
        >>> planner.plot.animation(path, str(planner), cost, expand)  # animation
        >>> planner.run()       # run both planning and animation

    References:
        [1] Theta*: Any-Angle Path Planning on Grids
        [2] Any-angle path planning on non-uniform costmaps
    """
    def __init__(self, start: tuple, goal: tuple, env: Grid, heuristic_type: str = "euclidean") -> None:
        super().__init__(start, goal, env, heuristic_type)

    def __str__(self) -> str:
        return "Theta*"

    def plan(self) -> tuple:
        """
        Theta* motion plan function.

        Returns:
            cost (float): path cost
            path (list): planning path
            expand (list): all nodes that planner has searched
        """
        # OPEN list (priority queue) and CLOSED list (hash table)
        OPEN = []
        heapq.heappush(OPEN, self.start)
        CLOSED = dict()

        while OPEN:
            node = heapq.heappop(OPEN)

            # exists in CLOSED list
            if node.current in CLOSED:
                continue

            # goal found
            if node == self.goal:
                CLOSED[node.current] = node
                cost, path, grounded = self.extractPath(CLOSED)
                return cost, path, list(CLOSED.values()), grounded

            for node_n in self.getNeighbor(node):
                # exists in CLOSED list
                if node_n.current in CLOSED:
                    continue

                # path1
                node_n.parent = node.current
                node_n.h = self.h(node_n, self.goal)

                node_p = CLOSED.get(node.parent)

                if node_p:
                    self.updateVertex(node_p, node_n)

                # goal found
                if node_n == self.goal:
                    heapq.heappush(OPEN, node_n)
                    break

                # update OPEN list
                heapq.heappush(OPEN, node_n)

            CLOSED[node.current] = node
        return [], [], [], []

    def updateVertex(self, node_p: Node, node_c: Node) -> None:
        """
        Update extend node information with current node's parent node.

        Parameters:
            node_p (Node): parent node
            node_c (Node): current node
        """
        if self.lineOfSight(node_c, node_p):
            # path 2
            if node_p.g + self.dist(node_c, node_p) <= node_c.g:
                node_c.g = node_p.g + self.dist(node_c, node_p)
                node_c.parent = node_p.current

    def lineOfSight(self, node1: Node, node2: Node) -> bool:
        """
        Judge collision when moving from node1 to node2 using Bresenham.

        Parameters:
            node1 (Node): start node
            node2 (Node): end node

        Returns:
            line_of_sight (bool): True if line of sight exists ( no collision ) else False
        """
        if node1.current in self.obstacles or node2.current in self.obstacles:
            return False

        # adapted to 3D with help of GPT
        # get start/end cells
        x0, y0, z0 = node2.current
        x1, y1, z1 = node1.current

        # differences along each axis (end - start)
        dx = x1 - x0  # difference in X
        dy = y1 - y0  # difference in Y
        dz = z1 - z0  # difference in Z

        # number of checkpoints we’ll inspect along the line
        steps = max(abs(dx), abs(dy), abs(dz))

        if steps == 0:
            return True

        # walk the line: interpolate a point between start and end at fraction t=i/steps
        for i in range(steps + 1):
            t = i / steps  # fraction between 0 and 1
            xi = round(x0 + t * dx)  # interpolate X (value between start and end)
            yi = round(y0 + t * dy)  # interpolate Y
            zi = round(z0 + t * dz)  # interpolate Z

            # check this checkpoint voxel
            if not (0 <= xi < self.env.x_range and 0 <= yi < self.env.y_range and 0 <= zi < self.env.z_range): # is in grid range?
                return False
            if (xi, yi, zi) in self.obstacles: # is it blocked by obstacle?
                return False
        return True
