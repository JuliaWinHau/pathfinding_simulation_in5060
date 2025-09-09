"""
Plot tools 2D
@author: huiming zhou
"""
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.ticker import MaxNLocator

from src.Pathfinding3D.environment3D.env import Env, Grid, Map
from src.Pathfinding3D.environment3D.node import Node


class Plot:
    def __init__(self, start, goal, env: Env):
        self.start = Node(start, start, 0, 0)
        self.goal = Node(goal, goal, 0, 0)
        self.env = env
        self.fig = plt.figure("planning")
        #self.ax = self.fig.add_subplot()
        # creation of the 3D figure
        self.ax = self.fig.add_subplot(111, projection='3d')

    def animation(self, path: list, name: str, cost: float = None, expand: list = None, history_pose: list = None,
                  predict_path: list = None, lookahead_pts: list = None, cost_curve: list = None,
                  ellipse: np.ndarray = None) -> None:
        name = name + "\ncost: " + str(cost) if cost else name
        self.plotEnv(name)
        if expand is not None:
            self.plotExpand(expand)
        if history_pose is not None:
            self.plotHistoryPose(history_pose, predict_path, lookahead_pts)
        if path is not None:
            self.plotPath(path)

        if cost_curve:
            plt.figure("cost curve")
            self.plotCostCurve(cost_curve, name)

        if ellipse is not None:
            self.plotEllipse(ellipse)

        plt.show()

    def plotEnv(self, name: str) -> None:
        '''
        Plot environment with static obstacles.

        Parameters
        ----------
        name: Algorithm name or some other information
        '''
        # plt.plot(self.start.x, self.start.y, self.start.z, marker="s", color="#ff0000")
        # plt.plot(self.goal.x, self.goal.y, self.goal.z, marker="s", color="#1155cc")
        self.ax.scatter(self.start.x, self.start.y, self.start.z, marker="s", color="#ff0000", label="start")
        self.ax.scatter(self.goal.x, self.goal.y, self.goal.z, marker="s", color="#1155cc", label="goal")

        # creating voxel obstacles
        if isinstance(self.env, Grid):
            # number of cells nx, ny, nz in the grid along x, y, z axes.
            nx, ny, nz = self.env.x_range, self.env.y_range, self.env.z_range

            # occupancy
            occ = np.zeros((nx, ny, nz), dtype=bool)
            for x, y, z in self.env.obstacles:
                if 0 <= x < nx and 0 <= y < ny and 0 <= z < nz:
                    occ[x, y, z] = True

            # edge-aligned coords (broadcastable)
            x_edges = (np.arange(nx + 1) - 0.5)[:, None, None]  # (nx+1,1,1)
            y_edges = (np.arange(ny + 1) - 0.5)[None, :, None]  # (1,ny+1,1)
            z_edges = (np.arange(nz + 1) - 0.5)[None, None, :]  # (1,1,nz+1)

            self.ax.voxels(x_edges, y_edges, z_edges, occ,
                           facecolors=(0.3, 0.3, 0.3, 0.35),
                           edgecolor='k', linewidth=0.3)

            # these two set_xlims and set_xticks is to remove the gap between the boundary voxels wall and the grid
            # match axes limits to the voxel edges
            self.ax.set_xlim(-0.5, nx - 0.5)
            self.ax.set_ylim(-0.5, ny - 0.5)
            self.ax.set_zlim(-0.5, nz - 0.5)

            # tidy ticks to land on voxel edges
            self.ax.set_xticks(np.arange(0, nx + 1, 1))
            self.ax.set_yticks(np.arange(0, ny + 1, 1))
            self.ax.set_zticks(np.arange(0, nz + 1, 1))

            # fewer integer-aligned ticks
            self.ax.xaxis.set_major_locator(MaxNLocator(nbins=8, integer=True, prune='both'))
            self.ax.yaxis.set_major_locator(MaxNLocator(nbins=8, integer=True, prune='both'))
            self.ax.zaxis.set_major_locator(MaxNLocator(nbins=8, integer=True, prune='both'))

            # smaller labels with a bit of spacing
            self.ax.tick_params(labelsize=10, pad=3)

            # true equal aspect in 3D (instead of plt.axis("equal"))
            self.ax.set_box_aspect((nx, ny, nz))

        if isinstance(self.env, Map):
            ax = self.fig.add_subplot()
            # boundary
            for (ox, oy, oz, w, d, h) in self.env.boundary:
                ax.add_patch(patches.Rectangle(
                        (ox, oy, oz), w, d, h,
                        edgecolor='black',
                        facecolor='black',
                        fill=True
                    )
                )
            # rectangle obstacles
            for (ox, oy,oz, w, h, d) in self.env.obs_rect:
                ax.add_patch(patches.Rectangle(
                        (ox, oy), w, d, h,
                        edgecolor='black',
                        facecolor='gray',
                        fill=True
                    )
                )
            # circle obstacles
            for (ox, oy, oz, r) in self.env.obs_circ:
                ax.add_patch(patches.Circle(
                        (ox, oy, oz), r,
                        edgecolor='black',
                        facecolor='gray',
                        fill=True
                    )
                )
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_zlabel('Z')
        self.ax.legend(loc="best")
        plt.title(name)


    def plotExpand(self, expand: list) -> None:
        '''
        Plot expanded grids using in graph searching.

        Parameters
        ----------
        expand: Expanded grids during searching
        '''
        if self.start in expand:
            expand.remove(self.start)
        if self.goal in expand:
            expand.remove(self.goal)

        count = 0
        if isinstance(self.env, Grid):
            for x in expand:
                count += 1
                #plt.plot(x.x, x.y, x.z, color="#dddddd", marker='s')
                self.ax.plot(x.x, x.y, x.z, color="#dddddd", marker='s')
                plt.gcf().canvas.mpl_connect('key_release_event',
                                            lambda event: [exit(0) if event.key == 'escape' else None])
                if count < len(expand) / 3:         length = 20
                elif count < len(expand) * 2 / 3:   length = 30
                else:                               length = 40
                if count % length == 0:             plt.pause(0.001)

        if isinstance(self.env, Map):
            for x in expand:
                count += 1
                if x.parent:
                    plt.plot([x.parent[0], x.x], [x.parent[1], x.y], [x.parent[2], x.z],
                       color="#dddddd", linestyle="-")
                    # self.ax.plot([x.parent[0], x.x], [x.parent[1], x.y], [x.parent[2], x.z],
                                 # color="#dddddd", linestyle="-")
                    plt.gcf().canvas.mpl_connect('key_release_event',
                                                 lambda event:
                                                 [exit(0) if event.key == 'escape' else None])
                    if count % 10 == 0:
                        plt.pause(0.001)

        plt.pause(0.01)

    def plotPath(self, path: list, path_color: str='#13ae00', path_style: str="-") -> None:
        '''
        Plot path in global planning.

        Parameters
        ----------
        path: Path found in global planning
        '''
        path_x = [path[i][0] for i in range(len(path))]
        path_y = [path[i][1] for i in range(len(path))]
        path_z = [path[i][2] for i in range(len(path))]
        #plt.plot(path_x, path_y, path_z, path_style, linewidth='2', color=path_color)
        #plt.plot(self.start.x, self.start.y, self.start.z, marker="s", color="#ff0000")
        #plt.plot(self.goal.x, self.goal.y, self.goal.z, marker="s", color="#1155cc")
        self.ax.plot(path_x, path_y, path_z, path_style, linewidth=2, color=path_color)
        self.ax.plot(self.start.x, self.start.y, self.start.z, marker="s", color="#ff0000")
        self.ax.plot(self.goal.x, self.goal.y, self.goal.z, marker="s", color="#1155cc")

    def plotAgent(self, pose: tuple, radius: float=1) -> None:
        '''
        Plot agent with specifical pose.

        Parameters
        ----------
        pose: Pose of agent
        radius: Radius of agent
        '''
        if len(pose) == 3:
            x, y, theta = pose
            z = 0
        else:
            x, y, z, theta = pose
        ref_vec = np.array([[radius / 2], [0]])
        rot_mat = np.array([[np.cos(theta), -np.sin(theta)],
                            [np.sin(theta),  np.cos(theta)]])
        end_pt = rot_mat @ ref_vec + np.array([[x], [y]])

        try:
            self.ax.artists.pop()
            for art in self.ax.get_children():
                if isinstance(art, matplotlib.patches.FancyArrow):
                    art.remove()
        except:
            pass

        self.ax.plot([x, float(end_pt[0])], [y, float(end_pt[1])], [z, z],
                     color="r", linewidth=3)
        self.ax.scatter(x, y, z, s=radius*100, color="r", alpha=0.6)

    def plotHistoryPose(self, history_pose, predict_path=None, lookahead_pts=None) -> None:
        lookahead_handler = None
        for i, pose in enumerate(history_pose):
            if i < len(history_pose) - 1:
                self.ax.plot([history_pose[i][0], history_pose[i + 1][0]], [history_pose[i][1], history_pose[i + 1][1]],
                             [history_pose[i][2], history_pose[i + 1][2]], c="#13ae00")
                if predict_path is not None:
                    self.ax.plot(predict_path[i][:, 0], predict_path[i][:, 1], predict_path[i][:, 2], c="#ddd")
            i += 1

            # agent
            self.plotAgent(pose)

            # lookahead
            if lookahead_handler is not None:
                lookahead_handler.remove()
            if lookahead_pts is not None:
                try:
                    lookahead_handler = self.ax.scatter(lookahead_pts[i][0], lookahead_pts[i][1], lookahead_pts[i][2], c="b")
                except:
                    lookahead_handler = self.ax.scatter(lookahead_pts[-1][0], lookahead_pts[-1][1], lookahead_pts[-1][2], c="b")

            plt.gcf().canvas.mpl_connect('key_release_event',
                                        lambda event: [exit(0) if event.key == 'escape' else None])
            if i % 5 == 0:             plt.pause(0.03)

    def plotCostCurve(self, cost_list: list, name: str) -> None:
        '''
        Plot cost curve with epochs using in evolutionary searching.

        Parameters
        ----------
        cost_list: Cost with epochs
        name: Algorithm name or some other information
        '''
        plt.plot(cost_list, color="b")
        plt.xlabel("epochs")
        plt.ylabel("cost value")
        plt.title(name)
        plt.grid()

    def plotEllipse(self, ellipse: np.ndarray, color: str = 'darkorange', linestyle: str = '--', linewidth: float = 2):
        plt.plot(ellipse[0, :], ellipse[1, :], linestyle=linestyle, color=color, linewidth=linewidth)

    def connect(self, name: str, func) -> None:
        self.fig.canvas.mpl_connect(name, func)

    def clean(self):
        plt.cla()

    def update(self):
        self.fig.canvas.draw_idle()

    @staticmethod
    def plotArrow(x, y, theta, length, color):
        angle = np.deg2rad(30)
        d = 0.5 * length
        w = 2

        x_start, y_start = x, y
        x_end = x + length * np.cos(theta)
        y_end = y + length * np.sin(theta)

        theta_hat_L = theta + np.pi - angle
        theta_hat_R = theta + np.pi + angle

        x_hat_start = x_end
        x_hat_end_L = x_hat_start + d * np.cos(theta_hat_L)
        x_hat_end_R = x_hat_start + d * np.cos(theta_hat_R)

        y_hat_start = y_end
        y_hat_end_L = y_hat_start + d * np.sin(theta_hat_L)
        y_hat_end_R = y_hat_start + d * np.sin(theta_hat_R)

        plt.plot([x_start, x_end], [y_start, y_end], color=color, linewidth=w)
        plt.plot([x_hat_start, x_hat_end_L], [y_hat_start, y_hat_end_L], color=color, linewidth=w)
        plt.plot([x_hat_start, x_hat_end_R], [y_hat_start, y_hat_end_R], color=color, linewidth=w)

    @staticmethod
    def plotCar(x, y, theta, width, length, color):
        theta_B = np.pi + theta

        xB = x + length / 4 * np.cos(theta_B)
        yB = y + length / 4 * np.sin(theta_B)

        theta_BL = theta_B + np.pi / 2
        theta_BR = theta_B - np.pi / 2

        x_BL = xB + width / 2 * np.cos(theta_BL)        # Bottom-Left vertex
        y_BL = yB + width / 2 * np.sin(theta_BL)
        x_BR = xB + width / 2 * np.cos(theta_BR)        # Bottom-Right vertex
        y_BR = yB + width / 2 * np.sin(theta_BR)

        x_FL = x_BL + length * np.cos(theta)               # Front-Left vertex
        y_FL = y_BL + length * np.sin(theta)
        x_FR = x_BR + length * np.cos(theta)               # Front-Right vertex
        y_FR = y_BR + length * np.sin(theta)

        plt.plot([x_BL, x_BR, x_FR, x_FL, x_BL],
                 [y_BL, y_BR, y_FR, y_FL, y_BL],
                 linewidth=1, color=color)

        Plot.plotArrow(x, y, theta, length / 2, color)