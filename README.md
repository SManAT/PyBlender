# PyBlender
This is info library for Python Scripts in Blender. I will collect here usefull tipps and
examples of scripts to deal with blender >2.8.

*Where is my Console?*

## Include Python modules (libraries)
```
import sys
sys.exec_prefix
import os
rootPath = os.path.abspath(os.path.join(os.path.dirname(__file__)))
libPath = os.path.join(rootPath, "test.py")
#add libPath to SystemPath
sys.path.insert(0, libPath)

print(sys.path)
```
