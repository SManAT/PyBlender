# Add a Path to the System Path of Python, relative to your blender File
import os
rootPath = os.path.abspath(os.path.join(os.path.dirname(bpy.data.filepath)))
libPath = os.path.join(rootPath, "")
# add libPath to SystemPath
sys.path.insert(0, libPath)
print(sys.path)
