import bpy
import os
import sys

"""
Mag. Stefan Hagmann 2020
This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/ or send a letter to Creative Commons,
PO Box 1866, Mountain View, CA 94042, USA.
"""

# Use the same Dir as Lib Dir
blend_file_path = bpy.data.filepath
lib_path = os.path.join(os.path.dirname(blend_file_path), ".")
if lib_path not in sys.path:
    sys.path.append(lib_path)

from Object import Object
from Collection import Collection


class ConsoleManager:
    """Keep Sysetmc Console open, track state"""

    _console_open = False

    @classmethod
    def show_system_console(cls):
        """Ensure system console is open (Windows only)"""
        if not cls._console_open:
            bpy.ops.wm.console_toggle()
            cls._console_open = True

    @classmethod
    def hide_system_console(cls):
        """Ensure system console is closed"""
        if cls._console_open:
            bpy.ops.wm.console_toggle()
            cls._console_open = False


class BlenderStuff:
    def __init__(self):
        # protected variables bind to instance
        self._scene = bpy.context.scene
        self._C = bpy.context
        self._D = bpy.data

        self._object = Object()
        self._collection = Collection()

        _ConsoleManager = ConsoleManager()
        _ConsoleManager.show_system_console()

    def show_system_console(self):
        """Show up the System Console"""
        # Check if the system console is visible
        for area in bpy.context.screen.areas:
            print(area)
            if area.type != "CONSOLE":
                bpy.ops.wm.console_toggle()

    def MakePolyLine(self, objname, curvename, cList, coll):
        """
        Creates a PolyLine from a list of 3D Vectors and adds it
        to Collection coll
        """
        # weight
        w = 1
        # 'POLY', 'BEZIER', 'BSPLINE', 'CARDINAL', 'NURBS'
        curvedata = self._D.curves.new(name=curvename, type="CURVE")
        curvedata.dimensions = "3D"

        objectdata = self._D.objects.new(objname, curvedata)
        # object origin
        objectdata.location = (0, 0, 0)

        polyline = curvedata.splines.new("POLY")
        polyline.points.add(len(cList) - 1)
        for num in range(len(cList)):
            x, y, z = cList[num]
            polyline.points[num].co = (x, y, z, w)

        # Remove object from Scene Collection
        bpy.ops.collection.objects_remove_all()

        # add it to our specific collection
        self._D.collections[coll].objects.link(objectdata)
