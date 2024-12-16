import maya.cmds as cmds
import random


x, y, z = [random.uniform(-10, 10) for _ in range(3)]
cmds.polyCube()
cmds.move(x, y, z)
