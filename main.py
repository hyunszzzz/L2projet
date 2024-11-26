from Flip import *


def main():
    window = ouvrirFenetre(WINDOW_SIZE, WINDOW_SIZE)
    grid = Grid(window, GRID_SIZE, CELL_SIZE)
    grid.create_grid()

    grid.draw_obstacles(10)

    ball_x, ball_y = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
    ball = Ball(ball_x, ball_y)
    ball.create_ball(window)

    window.actualiser()
    window.attendreClic()
    window.fermerFenetre()


