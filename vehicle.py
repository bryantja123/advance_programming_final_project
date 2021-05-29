from graphics import *
from projectile import Projectile


"""

        ///////////////////////////////////////////////////////////////
        /// Use this class alongside graphics.py and projectile.py! ///
        ///////////////////////////////////////////////////////////////



        A specialized class used to create moving vehicles for games
        in python made using graphics.py. This class utilizes the
        Projectile class to simulate the movement in a two dimensional
        environment.
    
"""


class Vehicle:
    
    #Graphical depiction of vehicle movement using red dots
    
    #Direction is determined by whether the
    #given velocity is positive or negative.
    
    def __init__(self, windowName, height, velocity, start):
        self.windowName = windowName
        self.height = height
        self.velocity = velocity
        self.start = start
        
    def spawn(self, windowName):
        self.proj = Projectile(0, self.velocity, self.height, self.start)
        self.icon = Image(Point(self.start , self.height), "reddot.gif")
        self.icon.draw(windowName)

    def getX(self):
        return self.proj.getX()

    def getY(self):
        return self.proj.getY()

    def update(self, time):
        self.proj.update(time)
        center = self.icon.getAnchor()
        dx = self.proj.getX() - center.getX()
        self.icon.move(dx, 0)

    def updateRight(self, time):
        self.proj.update(time)
        center = self.icon.getAnchor()
        dx = self.proj.getX() - center.getX()
        if(center.getX() < 6):
            self.icon.move(dx, 0)

    def updateLeft(self, time):
        self.proj.update(time)
        center = self.icon.getAnchor()
        dx = self.proj.getX() - center.getX()
        if(center.getX() > 0):
            self.icon.move(dx, 0)

    def despawn(self):
        self.icon.undraw()
