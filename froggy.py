
import math
from graphics import *
from projectile import Projectile


class frog():

    def __init__(self, windowName, height, velocity, start, image):
        self.windowName = windowName
        self.height = height
        self.velocity = velocity
        self.image = image

    def up(self):
        self.y += 45
    def down (self):
        self.y -= 45
    def right (self):
        self.x += 45
    def left (self):
        self.x -= 45

    def is_collision(self, other):
        x_collision = (math.fabs (self.x - other.x)* 2) < (self.width + other.width)
        y_collision = (math.fabs(self.y - other.y )*2) < (self.height + other.height)
        return (x_collision and y_collision)

    def spawn(self, windowName):
        self.icon= Image(Point(self.start, self.height), "froggy.gif")
        self.icon.draw(windowName)

