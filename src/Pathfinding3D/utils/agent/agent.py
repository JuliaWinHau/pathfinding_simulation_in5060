"""
@file: agent.py
@breif: Class for agent
@author: Yang Haodong, Wu Maojia
@update: 2024.3.29
"""
import math
import numpy as np
from abc import abstractmethod, ABC

class Agent(ABC):
    """
    Abstract class for agent.

    Parameters:
        px (float): initial x-position
        py (float): initial y-position
        theta (float): initial pose angle
    """
    def __init__(self, px, py, pz, theta) -> None:
        self.px = px
        self.py = py
        self.pz = pz
        self.theta = theta
        self.parameters = None

    def setParameters(self, **parameters) -> None:
        # other customer parameters
        self.parameters = parameters
        for param, val in parameters.items():
            setattr(self, param, val)

    @property
    def position(self):
        return (self.px, self.py, self.pz)

    @abstractmethod
    def kinematic(self, u, dt):
        pass

    @property
    @abstractmethod
    def state(self):
        pass


class Robot(Agent):
    """
    Class for robot.

    Parameters:
        px (float): initial x-position
        py (float): initial y-position
        theta (float): initial pose angle
        v (float): linear velocity
        w (float): angular velocity
    """
    def __init__(self, px, py, pz, theta, v, w, h) -> None:
        super().__init__(px, py, pz, theta)
        # velocity
        self.v = v
        self.w = w
        self.h = h # z velocity
        # history
        self.history_pose = []
    
    def __str__(self) -> str:
        return "Robot"
    
    def kinematic(self, u: np.ndarray, dt: float, replace: bool = True):
        """
        Run robot kinematic once.

        Parameters:
            u (np.ndarray): control command with [v, w]
            dt (float): simulation time
            replace (bool): update-self if true else return a new Robot object

        Returns:
            robot (Robot): a new robot object
        """
        new_state = self.lookforward(self.state, u, dt).squeeze().tolist()
        if replace:
            self.history_pose.append((self.px, self.py, self.pz, self.theta))
            self.px, self.py, self.pz, self.theta = new_state[0], new_state[1], new_state[2], new_state[3]
            self.v, self.w, self.h = new_state[4], new_state[5], new_state[6]
        else:
            new_robot = Robot(new_state[0], new_state[1], new_state[2], 
                new_state[3], new_state[4], new_state[5], new_state[6])
            new_robot.setParameters(**self.parameters)
            return new_robot
    
    def lookforward(self, state: np.ndarray, u: np.ndarray, dt: float) -> np.ndarray:
        """
        Run robot kinematic once but do not update.

        Parameters:
            state (np.ndarray): robot state with [x, y, theta, v, w]
            u (np.ndarray): control command with [v, w]
            dt (float): simulation time
            obstacles (set): set of obstacles with (x, y)

        Returns:
            new_state (np.ndarray (7x1)): new robot state with [x, y, z, theta, v, w, h]
        """
        F = np.array([[1, 0, 0, 0, 0, 0, 0], # x
                      [0, 1, 0, 0, 0, 0, 0], # y
                      [0, 0, 1, 0, 0, 0, 0], # z
                      [0, 0, 0, 1, 0, 0, 0], # theta
                      [0, 0, 0, 0, 0, 0, 0], # v
                      [0, 0, 0, 0, 0, 0, 0], # w
                      [0, 0, 0, 0, 0, 0, 0],]) # h
        B = np.array([[dt * math.cos(state[3]), 0, 0],  # x movement
                      [dt * math.sin(state[3]), 0, 0],  # y movement
                      [0, 0, dt],  # z movement
                      [0, dt, 0],  # theta change
                      [1, 0, 0],  # v update
                      [0, 1, 0],  # w update
                      [0, 0, 1]])  # h update
        new_state = F @ state + B @ u

        return new_state

    def reset(self) -> None:
        """
        Reset the state.
        """
        self.v = 0
        self.w = 0
        self.h = 0
        self.history_pose = []

    @property
    def state(self) -> None:
        """
        Get the state.

        Returns:
            state (np.ndarray (5x1)): robot state with [x, y, theta, v, w]
        """
        state = np.array([[self.px], [self.py], [self.pz], [self.theta], [self.v], [self.w], [self.h]])
        return state