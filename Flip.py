import random

from tkiteasy import *

GRID_SIZE = 50  # 50x50
WINDOW_SIZE = 600
CELL_SIZE = WINDOW_SIZE // GRID_SIZE
OBSTACLE_COUNT = 100

class Grid():

    def __init__(self, window, grid_size, cell_size):
        self.window = window
        self.grid_size = grid_size
        self.cell_size = cell_size
        self.obstacles = []  #list of obstacles

    def create_grid(self, window):
        for i in range(self.grid_size):
            y = i * self.cell_size
            self.window.dessinerLigne(0, y, self.grid_size * self.cell_size, y, "grey")

        for j in range(self.grid_size):
            x = j * self.cell_size
            self.window.dessinerLigne(x, 0, x, self.grid_size * self.cell_size, "grey")  # 수직선


    def draw_obstacles(self, num_obs):
        for _ in range(num_obs):
            x, y = random.randint(0, self.grid_size-1), random.randint(0, self.grid_size-1)
            obstacle_type = random.choice(["blue", "red", "green"])
            obstacle = Obstacle(x , y, obstacle_type)
            self.obstacles.append(obstacle)
            obstacle.create_obstacle(self.window)


class Ball():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = "yellow"

    def create_ball(self, window):

        center_x, center_y = self.x * CELL_SIZE + CELL_SIZE // 2, self.y * CELL_SIZE + CELL_SIZE // 2
        radius = CELL_SIZE // 3 # size ball
        window.dessinerCercle(center_x, center_y, radius, self.color)

class Obstacle():

    OBSTACLE_COLORS = {
        "blue": "blue",
        "red": "red",
        "green": "green"}
    def __init__(self, x, y, obstacle_type):
        self.x = x
        self.y = y
        self.type = obstacle_type
        self.color = self.OBSTACLE_COLORS[obstacle_type]

    def create_obstacle(self, window):
        grid_x, grid_y = self.x * CELL_SIZE, self.y * CELL_SIZE
        window.dessinerRectangle(grid_x, grid_y, grid_x + CELL_SIZE, grid_y + CELL_SIZE, self.color)
