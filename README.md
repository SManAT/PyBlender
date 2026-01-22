# PyBlender

This is info library for Python Scripts in Blender. I will collect here usefull tipps and
examples of scripts to deal with blender >2.8.

## Python and Blender

**Which Python does Blender use?**

```Python
import sys
sys.exec_prefix
```

Maybe that is _C:\Program Files\Blender Foundation\Blender 2.82\2.82\python_.
If you want to use another Version of Python, just delete this folder.

**Using pip**
Change within a terminal to the python path. Then you can use (Win)

```
.\bin\python.exe -m pip

.\bin\python.exe -m pip install mathutils
```

**Where is my Console?**
To see errors and hints have a look at the system console. To do This
_Window_ > _Toggle System Console_

## Some Basics for Beginners like me

**bpy.context.scene.collection**
Scene Master collection

**bpy.data.collections**
Main data structure and there are all collections

**bpy.ops.collection**
Collection Operators

## Include Python modules (libraries)

How to include your own libraries?
Example Structure

```
Main.blend
libs/
├─ Library.py
```

With this structure you can do something like that

```python
# Get the list of script paths
script_paths = bpy.utils.script_paths()
# Add your library path to the list
lib_path = os.path.join(os.path.dirname(bpy.data.filepath), "libs")
script_paths.append(lib_path)

# now you can import your own modules, e.q.
import Library
```

# Basic Example

```
import math
import sys
import os
import bpy

script_paths = bpy.utils.script_paths()
lib_path = os.path.join(os.path.dirname(bpy.data.filepath), "libs")
script_paths.append(lib_path)

from Collection import Collection
from BlenderStuff import BlenderStuff
from Object import Object

# variables
myScene = bpy.context.scene
C = bpy.context
D = bpy.data


# Main Program =================================================================
output_collection = "Output"
BStuff = BlenderStuff()
_Collection = Collection()
_Object = Object()
# delete if exists and create it new
_Collection.create_Collection(output_collection)

"""Main Entry Point"""

# 2Do

bpy.ops.wm.save_as_mainfile(filepath="pysaved.blend")

```

# Lindenmayer System in 3D

Use the lib LSystem3D.py.
The turtel has the following vectors in 3D

![turtle](/img/turtle.png "Axis")

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
