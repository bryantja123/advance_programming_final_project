'''
Advance Programming project
Group 9
Bryant Burgos 82874
Sebastian Castro 107094
Paola Osorio 96728
'''


from graphics import *
from projectile import Projectile

class Frog: #<--Placeholder

    def __init__(self, windowName):
        self.windowName = ""

    def drawFrog(self, windowName):
        pass

    def moveUp(self, windowName):
        pass

    def moveDown(self, windowName):
        pass

    def moveLeft(self, windowName):
        pass

    def moveRight(self, windowName):
        pass


class Vehicle:
    
    #Graphical depiction of moving vehicles
    
    def __init__(self, windowName, angle, velocity, height):
        self.windowName = ""
        #self.impact = False
        self.proj = Projectile(angle, velocity, height)
        self.icon = Circle(Point(0, height), 0.15)
        self.icon.setFill("red")
        self.icon.setOutline("red")
        self.icon.draw(windowName)


    def getX(self):
        return self.proj.getX()

    def getY(self):
        return self.proj.getY()

    
    def updateRight(self, time):
        self.proj.update(time)
        center = self.icon.getCenter()
        dx = self.proj.getX() - center.getX()
        self.icon.move(dx, 0)

    def updateLeft(self, time):
        self.proj.update(time)
        center = self.icon.getCenter()
        dx = center.getX() - self.proj.getX()
        self.icon.move(dx, 0)

    def moveRight(self):
        center = self.icon.getCenter()
        while (center.getX() < 6):
            update(35)
            self.updateRight(1/500)
            center = self.icon.getCenter()
            print(center.getX())
        self.undraw()
        pass
    
    def moveLeft(self):
        center = self.icon.getCenter()
        pass

    def hasImpacted():
        return self.impact

    def undraw(self):
        self.icon.undraw()
        pass

def main():

    win = GraphWin("Frogger", 600, 700, autoflush = False)
    win.setCoords(0, 0, 6, 7)
    win.setBackground("white")

    drawBackground(win)

    carSim = Vehicle(win, 0, 10, 2)
    carSim.moveRight()

    
##    for i in range(40):
##        update(35)
##        carSim.updateRight(1/500)

        
    

    
    win.getMouse()
    win.close()

    pass

#*******************************************************************************************

def drawBackground(windowName):

    windowName.setBackground("medium blue")
    
    road = Rectangle(Point(0, 0.5), Point(6, 3))
    road.setOutline("black")
    road.setFill("black")
    road.draw(windowName)

    medianStrip = Rectangle(Point(0, 0), Point(6, 0.5))
    medianStrip.setOutline("#800080")
    medianStrip.setFill("#800080")
    medianStrip.draw(windowName)

    upperMS = medianStrip.clone()
    upperMS.move(0, 3)
    upperMS.draw(windowName)


    frogLane = Rectangle(Point(0, 7), Point(6, 6))
    frogLane.setOutline("lime green")
    frogLane.setFill("lime green")
    frogLane.draw(windowName)



#*******************************************************************************************

main()

