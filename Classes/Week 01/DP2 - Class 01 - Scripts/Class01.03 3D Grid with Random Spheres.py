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
yCount = 50
zCount = 50
xScale = 10
yScale = 10
zScale = 10
rSphere = 5

def MakeSpheres(isCommon):
    for x in range(xCount):
        for y in range(yCount):
                for z in range(zCount):
                    if (isCommon):
                        sc.doc.Objects.AddSphere(Rhino.Geometry.Sphere(Rhino.Geometry.Point3d(x * xScale + xOffset, y * yScale,z * zScale), rSphere))
                    else:
                        rs.AddSphere((x * xScale + xOffset, y * yScale,z * zScale), rSphere)


if __name__=="__main__":
    xOffset = 0
    MakeSpheres(False)

    xOffset = (xCount + 1) * xScale
    MakeSpheres(True)
#    AddCircle_rs()