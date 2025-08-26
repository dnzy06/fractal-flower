# logic:
# F
# F -> F[+F][-F]

# F is a new branch

# We keep a stack of branch features (end point, length, width)
# to keep track of the data from the branch that we're trying to expand
# so we know what values to use for the next one

import math
from PIL import Image, ImageDraw
import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

class Branch():
    def __init__(self, endX, endY, length, width, depth, angle):
        self.endX = endX
        self.endY = endY
        self.depth = depth

        self.length = length
        self.width = width
        self.angle = angle

class Plant():
    def __init__(self, length, width, angle):
        self.plantCode = "F"
        self.lengthX = 300
        self.lengthY = 500
        self.startX = self.lengthX / 2
        self.startY = 400
        self.length = length
        self.angle = angle
        self.width = width
        self.frames = []
        self.depth = 1

    def expandCode(self):
        newCode = ""
        for i in range(len(self.plantCode)):
            if self.plantCode[i] == "F":
                newCode += "F[+F][-F]"
            else:
                newCode += self.plantCode[i]

        self.plantCode = newCode
        self.depth += 1

    def rotateEndPoint(self, startX, startY, length, angle):
        endX = startX + length * math.sin(angle)
        endY = startY - length * math.cos(angle)
        return endX, endY
    
    def drawPlant(self):
        branchStack = []

        endX = self.startX
        endY = self.startY - self.length

        self.img = Image.new('RGB', (self.lengthX, self.lengthY), color='white')
        self.draw = ImageDraw.Draw(self.img)

        self.draw.line([(self.startX, self.startY), (endX, endY)], fill='green', width=self.width)
        self.frames.append(np.array(self.draw._image.copy()))

        print('og length: ', self.length)
        mostRecentBranch = Branch(endX, endY, self.length, self.width, 1, 0)

        branchStack.append(mostRecentBranch)

        for i in range(1, len(self.plantCode)):
            if self.plantCode[i] == "[":
                mostRecentBranch = branchStack.pop()
                count = 0

            if self.plantCode[i] == "+":
                direction = "+"

            if self.plantCode[i] == "-":
                direction = "-"

            if self.plantCode[i] == "F":
                count += 1
                print(direction)
                startX = mostRecentBranch.endX
                startY = mostRecentBranch.endY
                length = mostRecentBranch.length * 0.5
                if mostRecentBranch.width != 1:
                    width =- 1
                depth = mostRecentBranch.depth + 1

                if direction == "+":
                    angle = mostRecentBranch.angle + self.angle
                    endX, endY = self.rotateEndPoint(startX, startY, length, angle)
                    print("direction positive, print endx and endy")
                    print(endX)
                    print(endY)
                    print(angle)
                    print(startX)
                    print(startY)
                    print(length)

                if direction == "-":
                    angle = mostRecentBranch.angle - self.angle
                    endX, endY = self.rotateEndPoint(startX, startY, length, angle)

                fillColor = 'green'
                if (depth == self.depth):
                    fillColor = 'red'

                print(startX)
                print(startY)
                print(endX)
                print(endY)
                self.draw.line([(startX, startY), (endX, endY)], fill=fillColor, width=width)
                self.frames.append(np.array(self.draw._image.copy()))

                newBranch = Branch(endX, endY, length, width, depth + 1, angle)
                branchStack.append(newBranch)

            if self.plantCode[i] == "]":
                if count != 2:
                    branchStack.append(mostRecentBranch)

        self.img.save('visualization/plantIterative.png')

plant = Plant(100, 3, math.pi/6)
depth = 3

for i in range(depth - 1):
    plant.expandCode()
    print(plant.plantCode)

plant.drawPlant()




            

        
