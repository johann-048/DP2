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


xCount = 10
yCount = 5
zCount = 5
xScale = 10
yScale = 10
zScale = 10
rSphere = 5

listValues = np.arange(0, 2 * math.pi, 2 * math.pi / xCount)
print(listValues)


# Print out the coordinates of each point
for x in listValues:

     for y in listValues:
        # z = math.sin(x)
        z = math.sin(x) + math.sin(y)
        colorval = (z+2) / 4.0 * 255
        print(x, " ", colorval)
        pointId = rs.AddSphere( (x * xScale, y * yScale , z * zScale ), rSphere)
        rs.ObjectColor(pointId, [255 - colorval, colorval, 0])
         

 # done!