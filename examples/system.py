#Add a Path to the System Path of Python, relative to your blender File
import os
script_paths = bpy.utils.script_paths()
lib_path = os.path.join(os.path.dirname(bpy.data.filepath), "libs")
script_paths.append(lib_path)

