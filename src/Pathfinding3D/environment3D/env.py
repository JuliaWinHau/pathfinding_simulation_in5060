"""
@file: env.py
@breif: 2-dimension environment
@author: Winter
@update: 2023.1.13
"""
from math import sqrt
from abc import ABC, abstractmethod
from scipy.spatial import cKDTree
import numpy as np
from src.Pathfinding3D.environment3D.node import Node

class Env(ABC):
    """
    Class for building 2-d workspace of robots.

    Parameters:
        x_range (int): x-axis range of enviroment
        y_range (int): y-axis range of environmet
        eps (float): tolerance for float comparison

    Examples:
        >>> from python_motion_planning.utils import Env
        >>> env = Env(30, 40)
    """
    def __init__(self, x_range: int, y_range: int, z_range: int, eps: float = 1e-6) -> None:
        # size of environment
        self.x_range = x_range  
        self.y_range = y_range
        self.z_range = z_range
        self.eps = eps

    @property
    def grid_map(self) -> set:
        return {(i, j, k) for i in range(self.x_range) for j in range(self.y_range) for k in range(self.z_range)}

    @abstractmethod
    def init(self) -> None:
        pass

class Grid(Env):
    """
    Class for discrete 2-d grid map.

    Parameters:
        x_range (int): x-axis range of enviroment
        y_range (int): y-axis range of environmet
    """
    def __init__(self, x_range: int, y_range: int, z_range :int) -> None:
        super().__init__(x_range, y_range, z_range)
        # allowed motions
        # self.motions = [Node((-1, 0), None, 1, None), Node((-1, 1),  None, sqrt(2), None),
                        # Node((0, 1),  None, 1, None), Node((1, 1),   None, sqrt(2), None),
                        # Node((1, 0),  None, 1, None), Node((1, -1),  None, sqrt(2), None),
                        # Node((0, -1), None, 1, None), Node((-1, -1), None, sqrt(2), None)]

        # allowed directions in 3D based on Euclidean distance
        self.motions = [
        # movement along single axis
        Node((-1, 0, 0), None, 1, None),  # west
        Node((1, 0, 0), None, 1, None),  # east
        Node((0, -1, 0), None, 1, None),  # south
        Node((0, 1, 0), None, 1, None),  # north
        Node((0, 0, -1), None, 1, None),  # down
        Node((0, 0, 1), None, 1, None),  # up

        # movement along 2 axes
        Node((-1, 1, 0), None, sqrt(2), None),  # northwest
        Node((1, 1, 0), None, sqrt(2), None),  # northeast
        Node((-1, -1, 0), None, sqrt(2), None),  # southwest
        Node((1, -1, 0), None, sqrt(2), None),  # southeast
        Node((-1, 0, -1), None, sqrt(2), None),  # west + down
        Node((-1, 0, 1), None, sqrt(2), None),  # west + up
        Node((1, 0, -1), None, sqrt(2), None),  # east + down
        Node((1, 0, 1), None, sqrt(2), None),  # east + up
        Node((0, -1, -1), None, sqrt(2), None),  # south + down
        Node((0, -1, 1), None, sqrt(2), None),  # south + up
        Node((0, 1, -1), None, sqrt(2), None),  # north + down
        Node((0, 1, 1), None, sqrt(2), None),  # north + up

        # movement along 3 axes
        Node((-1, -1, -1), None, sqrt(3), None),  # southwest + down
        Node((-1, -1, 1), None, sqrt(3), None),  # southwest + up
        Node((-1, 1, -1), None, sqrt(3), None),  # northwest + down
        Node((-1, 1, 1), None, sqrt(3), None),  # northwest + up
        Node((1, -1, -1), None, sqrt(3), None),  # southeast + down
        Node((1, -1, 1), None, sqrt(3), None),  # southeast + up
        Node((1, 1, -1), None, sqrt(3), None),  # northeast + down
        Node((1, 1, 1), None, sqrt(3), None)]  # northeast + up


        # obstacles
        self.obstacles = None
        self.obstacles_tree = None
        self.init()
    
    def init(self) -> None:
        """
        Initialize grid map.
        """
        x, y, z = self.x_range, self.y_range, self.z_range
        obstacles = set()

        # boundary of environment
        # XY faces
        for i in range(x):
            for j in range(y):
                obstacles.add((i, j, 0))  # Floor
                obstacles.add((i, j, z - 1))  # Ceiling

        # XZ faces
        for i in range(x):
            for k in range(z):
                obstacles.add((i, 0, k))  # Front wall
                obstacles.add((i, y - 1, k))  # Back wall

        # YZ faces
        for j in range(y):
            for k in range(z):
                obstacles.add((0, j, k))  # Left wall
                obstacles.add((x - 1, j, k))  # Right wall

        self.update(obstacles)

    def update(self, obstacles):
        self.obstacles = obstacles 
        self.obstacles_tree = cKDTree(np.array(list(obstacles)))


class Map(Env):
    """
    Class for continuous 2-d map.

    Parameters:
        x_range (int): x-axis range of enviroment
        y_range (int): y-axis range of environmet
    """
    def __init__(self, x_range: int, y_range: int, z_range: int) -> None:
        super().__init__(x_range, y_range, z_range)
        self.boundary = None
        self.obs_circ = None
        self.obs_rect = None
        self.init()

    def init(self):
        """
        Initialize map.
        """
        x, y, z = self.x_range, self.y_range, self.z_range

        self.boundary = [
            [0, 0, 0, 1, y, z],  # Left wall
            [0, y, 0, x, 1, z],  # Back wall
            [1, 0, 0, x, 1, z],  # Front wall
            [x, 1, 0, 1, y, z],  # Right wall
            [0, 0, 0, x, y, 1],  # Floor
            [0, 0, z, x, y, 1]   # ceiling
        ]
        self.obs_rect = []
        self.obs_circ = []


    def update(self, boundary=None, obs_circ=None, obs_rect=None):
        self.boundary = boundary if boundary else self.boundary
        self.obs_circ = obs_circ if obs_circ else self.obs_circ
        self.obs_rect = obs_rect if obs_rect else self.obs_rect
