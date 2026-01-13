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

xCount = 5
yCount = 5
zCount = 5
xScale = 10
yScale = 10
zScale = 10
rSphere = 5
lastpt = rs.AddPoint((0,0,0))

# Your Code Here!

for x in range(xCount):
    for y in range(yCount):
        for z in range(zCount):
            thispt = rs.AddPoint( [x * xScale ,y * yScale,z * zScale] )
            if z > 0:
                rs.AddLine(lastpt, thispt)
            print(x)
            lastpt = thispt


 # done!