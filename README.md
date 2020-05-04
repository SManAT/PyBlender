# PyBlender
This is info library for Python Scripts in Blender. I will collect here usefull tipps and
examples of scripts to deal with blender >2.8.

**Prerequisite**
```Python
pip install mathutils
```

**Where is my Console?**
To see errors and hints have a look at the system console. To do This
*Window* > *Toggle System Console*

## Some Basics for Beginners like me
**bpy.context.scene.collection**
Scene Master collection

**bpy.data.collections**
Main data structure and there are all collections

**bpy.ops.collection**
Collection Operators

## Include Python modules (libraries)
How to include your own libraries? You have to change the Python SystemPath (i call it).
```python
import sys
sys.exec_prefix

import os
rootPath = os.path.abspath(os.path.join(os.path.dirname(__file__)))
libPath = os.path.join(rootPath, "test.py")
#add libPath to SystemPath
sys.path.insert(0, libPath)

print(sys.path)
```

# Lindenmayer System in 3D
Use the lib LSystem3D.py. The turtel has the following vectors in 3D
![turtle](/img/turtle.png  "Axis")



## First Test in Blender
```python
import bpy
import os
import sys

rootPath = os.path.abspath(os.path.join(os.path.dirname(bpy.data.filepath)))
libPath = os.path.join(rootPath, "../lib")
sys.path.insert(0, libPath)

from BlenderStuff import BlenderStuff
from LSystem3D import LSystem3D
from mathutils import Vector

#Lindenmayer System ----------------------------------
LSys = LSystem3D()
#no iterations here, just a test
LSys._alpha = 120
LSys.rotate_around_H(45)
#Draw a equilateral triangle
LSys._code = "F&F&F"

LSys.calculatePoints()  
LSys.printVectorlist()
listOfVectors = LSys.getVectorList()

#Blender Part ---------------------------------------
BStuff = BlenderStuff()
coll = "Path"
BStuff.create_Collection(coll)

BStuff.MakePolyLine("LSysTest", "LSysTest", listOfVectors, coll)
```
