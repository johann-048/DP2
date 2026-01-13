#! python3
"""Testing pip install specific packages"""
# r: numpy

import rhinoscriptsyntax as rs
import scriptcontext as sc

import System
import System.Collections.Generic
import Rhino
import random
import math
import numpy as np


xCount = 50
yCount = 5
zCount = 5
xScale = 10
yScale = 10
zScale = 10
rSphere = 5

listValues = np.arange(0, 2 * math.pi, 2 * math.pi / xCount)
print(listValues)
rect1 = rs.GetRectangle()


# Print out the coordinates of each point
for x in listValues:
        y=0
    # for y in listValues:
        z = math.sin(x) + math.sin(y)
        pointId = rs.AddPoint( (x * xScale + rect1[0][0], y * yScale + rect1[0][1], z * zScale + rect1[0][2]))
        #print(sphereId)
        rs.ObjectColor(pointId, [int(random.random() * 255), int(random.random() * 255), \
        int(random.random() * 255) ])   
         

 # done!