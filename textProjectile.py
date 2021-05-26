# textProjectile.py

"""
projectile.py, original written by John Zelle
for Python Programming: An Introduction to
                        Computer Science (3rd Ed.)

Provides a simple class for modeling the 
flight of projectiles.
"""
   
from math import sin, cos, radians

class Projectile:

    """Simulates the flight of simple projectiles near the earth's
    surface, ignoring wind resistance. Tracking is done in two
    dimensions, height (y) and distance (x)."""

    def __init__(self, angle, velocity, yinit, xinit):              #changed xpos to xinit
        """Create a projectile with given launch angle, initial"""  #insead of just starting
        """velocity and position."""                                #every time at 0
        self.xpos = xinit
        self.ypos = yinit
        theta = radians(angle)
        self.xvel = velocity * cos(theta)
        self.yvel = velocity * sin(theta)

    def update(self, time):
        """Update the state of this projectile to move it time seconds
        farther into its flight"""
        self.xpos = self.xpos + time * self.xvel
        yvel1 = self.yvel - 9.8 * time
        self.ypos = self.ypos + time * (self.yvel + yvel1) / 2.0
        self.yvel = yvel1

    def getY(self):
        "Returns the y position (height) of this projectile."
        return self.ypos

    def getX(self):
        "Returns the x position (distance) of this projectile."
        return self.xpos

    def setY(self, newY):
        "Sets the y position (height) of this projectile."
        self.ypos = newY

    def setX(self, newX):
        "Sets the x position (distance) of this projectile."
        self.xpos = newX

    def setAngle(self, angle):
        theta = radians(angle)
        self.xvel = velocity * cos(theta)
        self.yvel = velocity * sin(theta)
        
