import math
from PIL import Image, ImageDraw
import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

class Node():
    def __init__(self, startX, startY, length, width, depth, angle):
        self.startX = startX
        self.startY = startY
        self.depth = depth

        self.length = length
        self.width = width
        self.angle = angle

class Plant():
    def __init__(self, length, width, angle, depth):
        self.plantCode = "AB"
        self.lengthX = 300
        self.lengthY = 500
        self.startX = self.lengthX / 2
        self.startY = 400
        self.length = length
        self.angle = angle
        self.width = width
        self.frames = []
        self.depth = depth

    def rotateEndPoint(self, startX, startY, length, angle):
        endX = startX + length * math.sin(angle)
        endY = startY - length * math.cos(angle)
        return endX, endY
    
    def drawPlant(self):
        self.img = Image.new('RGB', (self.lengthX, self.lengthY), color='white')
        self.draw = ImageDraw.Draw(self.img)
        
        endX = self.startX
        endY = self.startY - self.length
        self.draw.line([(self.startX, self.startY), (endX, endY)], fill='green', width=self.width)
        self.frames.append(np.array(self.draw._image.copy()))

        nodeQueue = []
        startingNode = Node(endX, endY, self.length, self.width, 1, 0)
        nodeQueue.append(startingNode)

        while (not len(nodeQueue) == 0):
            currNode = nodeQueue.pop(0)
            currDepth = currNode.depth
            currLength = currNode.length
            width = currNode.width

            if (currDepth > self.depth):
                break

            if width != 1:
                width = width - 1

            if currDepth == self.depth:
                color = 'red'

            else:
                color = 'green'

            startX = currNode.startX
            startY = currNode.startY

            # draw left branch
            length = currLength * random.uniform(0.5, 0.7)
            angle = currNode.angle + self.angle + random.uniform(-math.pi/15, math.pi/10)
            endX, endY = self.rotateEndPoint(startX, startY, length, angle)
            self.draw.line([(startX, startY), (endX, endY)], fill=color, width=width)
            self.frames.append(np.array(self.draw._image.copy()))

            # append left node
            leftNode = Node(endX, endY, length, width, currDepth + 1, angle)
            nodeQueue.append(leftNode)

            # draw center branch
            angle = currNode.angle + random.uniform(-math.pi/15, math.pi/10)
            length = currLength * random.uniform(0.5, 0.7)
            endX, endY = self.rotateEndPoint(startX, startY, length, angle)
            self.draw.line([(startX, startY), (endX, endY)], fill=color, width=width)
            self.frames.append(np.array(self.draw._image.copy()))

            # append center node
            centerNode = Node(endX, endY, length, width, currDepth + 1, angle)
            nodeQueue.append(centerNode)

            # draw right branch
            angle = currNode.angle - self.angle + random.uniform(-math.pi/15, math.pi/10)
            length = currLength * random.uniform(0.5, 0.7)
            endX, endY = self.rotateEndPoint(startX, startY, length, angle)
            self.draw.line([(startX, startY), (endX, endY)], fill=color, width=width)
            self.frames.append(np.array(self.draw._image.copy()))

            # append right node
            rightNode = Node(endX, endY, length, width, currDepth + 1, angle)
            nodeQueue.append(rightNode)

        self.img.save('visualization/plantIterative.png')

    def createFramesToAnimate(self):
        print(len(self.frames))
        framesToAnimate = []
        for i, frame in enumerate(self.frames):
            if i % 100 == 0:
                framesToAnimate.append(frame)

        return framesToAnimate

plant = Plant(100, 3, math.pi/8, 10)
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
        
