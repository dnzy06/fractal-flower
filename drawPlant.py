from PIL import Image, ImageDraw
import math
import random

class Plant():
    def __init__(self, depth, length, angle):

        self.depth = depth
        self.lengthX = 300
        self.lengthY = 500
        self.startX = self.lengthX / 2
        self.startY = 400
        self.length = length
        self.angle = angle

        self.img = Image.new('RGB', (self.lengthX, self.lengthY), color='white')
        self.draw = ImageDraw.Draw(self.img)

    def rotateEndPoint(self, startX, startY, length, angle):
        endX = startX + length * math.sin(angle)
        endY = startY - length * math.cos(angle)
        return endX, endY
    
    def drawPlant(self):
        self.drawPlantHelper(self.startX, self.startY, 0, self.length, self.depth)
        self.img.show()
        self.img.save('visualization/plant.png')

    
    def drawPlantHelper(self, currStartX, currStartY, currAngle, currLength, currDepth):
        fillColor = 'black'

        if (currDepth == 0):
            return
        
        if (currDepth == 1):
            fillColor = 'red'
        
        endX, endY = self.rotateEndPoint(currStartX, currStartY, currLength, currAngle)
        self.draw.line([(currStartX, currStartY), (endX, endY)], fill=fillColor, width=1)

        self.drawPlantHelper(endX, endY, currAngle + self.angle + random.uniform(-math.pi/20, math.pi/10), currLength * random.uniform(0.5, 0.7), currDepth - 1)
        self.drawPlantHelper(endX, endY, currAngle + random.uniform(-math.pi/15, math.pi/10), currLength * random.uniform(0.5, 0.7), currDepth - 1)
        self.drawPlantHelper(endX, endY, currAngle - self.angle + random.uniform(-math.pi/20, math.pi/10), currLength * random.uniform(0.5, 0.7), currDepth - 1)

plant = Plant(12, 100, math.pi/8)
plant.drawPlant()

