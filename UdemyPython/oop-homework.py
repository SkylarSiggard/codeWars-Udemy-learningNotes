import math 
#! Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.
class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2 
    
    def distance(self):
        return math.sqrt((self.coor2[0]-self.coor1[0])**2+(self.coor2[1]-self.coor1[1])**2)
        #! or if you didnt want to use math 
        #* (self.coor2[0]-self.coor1[0])**2+(self.coor2[1]-self.coor1[1])**2)**0.5
    
    def slope(self):
        return (self.coor2[1]-self.coor1[1]) / (self.coor2[0]-self.coor1[0])
# EXAMPLE OUTPUT
coordinate1 = (3,2)
coordinate2 = (8,10)
li = Line(coordinate1,coordinate2)
li.distance()
# out 9.433981132056603
# out 1.6 
li.slope()

#! find the volume and surface area 
class Cylinder:
    pi = 3.14
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius 
        
    def volume(self):
        return 3.14 * self.radius**2 * self.height
    
    def surface_area(self):
        return 2 * 3.14 * self.radius * self.height + (3.14 * self.radius**2) * 2 
# EXAMPLE OUTPUT
c = Cylinder(2,3)
c.volume()
#out 56.52
c.surface_area()
#out 94.2