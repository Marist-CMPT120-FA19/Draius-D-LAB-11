#Draius Disimone Lab 11
#draius.disimone1@marist.edu

#import math lib
import math

class Sphere:
    
#defining __init method
    def __init__(self , radius):
        self.radius = radius
        self.surfaceArea = (4/3) * math.pi * self.radius ** 3
        self.volume = 4 * math.pi * self.radius ** 2
#defining radius        
    def getRadius(self):
        return self.radius
#surface area        
    def getSurfaceArea(self):
        return self.surfaceArea
#volume        
    def getVolume(self):
        return self.volume
        
def run():
    radius = float(input("Enter the radius of your sphere: "))
    obj = Sphere(radius)
    print("VOLUME of Sphere = " , obj.getVolume())
    print("SURFACE AREA of Sphere = " , obj.getSurfaceArea())
    
if __name__ == '__main__':
    run()
