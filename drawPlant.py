from PIL import Image, ImageDraw
import math
import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

class Plant():
    def __init__(self, depth, length, angle, color):

        self.depth = depth
        self.lengthX = 300
        self.lengthY = 500
        self.startX = self.lengthX / 2
        self.startY = 400
        self.length = length
        self.angle = angle
        self.width = 3
        self.color = color

        self.img = Image.new('RGB', (self.lengthX, self.lengthY), color='white')
        self.draw = ImageDraw.Draw(self.img)

        self.frames = []

    def rotateEndPoint(self, startX, startY, length, angle):
        endX = startX + length * math.sin(angle)
        endY = startY - length * math.cos(angle)
        return endX, endY
    
    def drawPlant(self):
        self.drawPlantHelper(self.startX, self.startY, 0, self.length, self.depth, self.width)
        self.img.save('visualization/plant.png')
    
    def drawPlantHelper(self, currStartX, currStartY, currAngle, currLength, currDepth, currWidth):
        fillColor = 'green'

        if (currDepth == 0):
            self.frames.append(np.array(self.draw._image.copy()))
            return
        
        if (currDepth == 1):
            fillColor = self.color
        
        endX, endY = self.rotateEndPoint(currStartX, currStartY, currLength, currAngle)
        self.draw.line([(currStartX, currStartY), (endX, endY)], fill=fillColor, width=currWidth)

        if currWidth != 1:
            newWidth = currWidth - 1
        
        else:
            newWidth = currWidth

        self.drawPlantHelper(endX, endY, currAngle + self.angle + random.uniform(-math.pi/20, math.pi/10), currLength * random.uniform(0.5, 0.7), currDepth - 1, newWidth)
        self.drawPlantHelper(endX, endY, currAngle + random.uniform(-math.pi/15, math.pi/10), currLength * random.uniform(0.5, 0.7), currDepth - 1, newWidth)
        self.drawPlantHelper(endX, endY, currAngle - self.angle + random.uniform(-math.pi/20, math.pi/10), currLength * random.uniform(0.5, 0.7), currDepth - 1, newWidth)

    def createFramesToAnimate(self):
        framesToAnimate = []
        for i, frame in enumerate(self.frames):
            if i % 100 == 0:
                framesToAnimate.append(frame)

        return framesToAnimate
    
plant = Plant(10, 100, math.pi/8, 'red')
plant.drawPlant()

frames = plant.createFramesToAnimate()
fig, ax = plt.subplots()
im = ax.imshow(frames[0])

def animate(frame):
   im.set_array(frames[frame])
   return [im]

ani = animation.FuncAnimation(fig, animate, frames=len(frames), 
                           interval=2, repeat=False)
plt.show()

plant = Plant(10, 100, math.pi/8, 'pink')
plant.drawPlant()

frames = plant.createFramesToAnimate()
fig, ax = plt.subplots()
im = ax.imshow(frames[0])

def animate(frame):
   im.set_array(frames[frame])
   return [im]

ani = animation.FuncAnimation(fig, animate, frames=len(frames), 
                           interval=2, repeat=False)
plt.show()





