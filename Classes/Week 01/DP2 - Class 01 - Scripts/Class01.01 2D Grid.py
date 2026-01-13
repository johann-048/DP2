#! python3
"""Testing "pip" install speci


fic packages"""
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
yCount = 10
zCount = 10
xScale = 10
yScale = 10
zScale = 10
rSphere = 3
modulo = 3
cutoff = 0.1

# Print out the coordinates of each point
for x in range(xCount):
     for y in range(yCount):
             for z in range(zCount):
                a = random.random()
                print(a)
                if (a < cutoff): sphereId = rs.AddSphere((x * xScale, y * yScale, z * zScale), rSphere)
      

 # done!