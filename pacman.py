import turtle
import ctypes
import collections
import tkinter as tk
from grids import get_grid
import search
from heuristic import EuclideanDistance


class Maze(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("images/map.gif")
        self.penup()
        self.speed(0)


class Forage(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("images/strawberry.gif")
        self.penup()
        self.speed(0)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


class Space(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.speed(0)


class Sprite(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("images/Pacman_Right.gif")
        self.speed(0)


class Pacman:
    space = []
    wn = None
    res_x, res_y = None, None
    map_graph = None
    maze, sprite, forage = None, None, None
    walls, forages = [], []
    first_pacman_position = (None, None)

    def __init__(self) -> None:
        self.wn = turtle.Screen()
        self.setup()
        self.maze = Maze()
        self.sprite = Sprite()
        self.forage = Forage()

    def setup(self):
        self.res_x, self.res_y = (
            ctypes.windll.user32.GetSystemMetrics(0),
            ctypes.windll.user32.GetSystemMetrics(1),
        )
        self.wn.bgcolor("black")
        self.wn.title("Pacman Game")
        self.wn.setup(width=.99, height=.90, startx=0, starty=0)
        self.wn.register_shape("images/map.gif")
        self.wn.register_shape("images/strawberry.gif")
        self.wn.register_shape("images/Pacman_Right.gif")
        self.map_graph = collections.defaultdict(list)

    def discoverMaze(self, x_pos, y_pos):
        if (x_pos+24, y_pos) in self.space:
            (
                self.map_graph[self.space.index((x_pos, y_pos))]
                .append(self.space.index((x_pos+24, y_pos)))
            )
        if (x_pos-24, y_pos) in self.space:
            (
                self.map_graph[self.space.index((x_pos, y_pos))]
                .append(self.space.index((x_pos-24, y_pos)))
            )
        if (x_pos, y_pos+24) in self.space:
            (
                self.map_graph[self.space.index((x_pos, y_pos))]
                .append(self.space.index((x_pos, y_pos+24)))
            )
        if (x_pos, y_pos-24) in self.space:
            (
                self.map_graph[self.space.index((x_pos, y_pos))]
                .append(self.space.index((x_pos, y_pos-24)))
            )

        last_index = self.space.index((x_pos, y_pos)) + 1
        if last_index != len(self.space):
            x_y_pos = self.space[last_index]
            self.discoverMaze(x_y_pos[0], x_y_pos[1])

    def move(self, path_list, endStamp):
        for index in path_list:
            x_y_position = self.space[index]
            self.sprite.goto(x_y_position[0], x_y_position[1])
        self.sprite.goto(self.space[endStamp])

    def setupMaze(self, grid):
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                character = grid[y][x]
                screen_x = ((-self.res_x/2)+(self.res_x-960)/2) + (x * 24)
                screen_y = (self.res_y/3) - (y * 24)
                if character == "+":
                    self.maze.goto(screen_x, screen_y)
                    self.maze.stamp()
                    self.walls.append((screen_x, screen_y))
                elif character == "f":
                    self.forage.goto(screen_x, screen_y)
                    self.forage.stamp()
                    self.forages.append((screen_x, screen_y))
                    self.space.append((screen_x, screen_y))
                elif character == "s":
                    self.sprite.speed(1)
                    self.sprite.goto(screen_x, screen_y)
                    self.first_pacman_position = (screen_x, screen_y)
                    self.sprite.pen(
                        fillcolor="black", pencolor="yellow", pensize=2,
                    )
                    self.space.append((screen_x, screen_y))
                else:
                    self.space.append((screen_x, screen_y))

    def get_index_of_food(self, value):
        for index, item in enumerate(self.forages):
            if item == value:
                return index

    def find_nearest_food(self, start_position):
        foods_list = self.forages.copy()
        temp_list, result_list = [], []

        for _ in range(len(self.forages)):

            for item in foods_list:
                dis = EuclideanDistance(start_position, item)
                index = self.get_index_of_food(item)
                temp_list.append((index, dis, item))

            temp_list.sort(key=lambda x: x[1])
            result_list.append(temp_list[0])
            start_position = temp_list[0][2]
            foods_list.remove(temp_list[0][2])
            temp_list.clear()

        return [x[0] for x in result_list]

    def run_algorithm_function(self, priority_food):
        last_forages_index = 0
        for i in priority_food:
            search.path_list.clear()
            aStar_came_from = search.aStar(
                graph=self.map_graph,
                start_index=last_forages_index,
                end_index=self.space.index(self.forages[i]),
                x_y_start=(self.sprite.xcor(), self.sprite.ycor()),
                x_y_end=(self.forages[i]),
            )
            search.traverse_back(
                came_from=aStar_came_from,
                end_index=self.space.index(self.forages[i]),
                start_position=last_forages_index,
            )
            last_forages_index = self.space.index(self.forages[i])
            self.move(search.path_list, last_forages_index)

    def solve(self, count):
        grid = get_grid(count)
        self.setupMaze(grid)
        self.discoverMaze(self.sprite.xcor(), self.sprite.ycor())
        priority_food = self.find_nearest_food(self.first_pacman_position)
        self.run_algorithm_function(priority_food)
        tk.mainloop()


if __name__ == '__main__':
    while True:
        count_foods = int(input("Enter count of food? (1, 2, 3, 4)? "))
        if count_foods in range(1, 5):
            break
    pacman = Pacman()
    pacman.solve(count_foods)
