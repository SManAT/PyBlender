import bpy

"""
Mag. Stefan Hagmann 2020
This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/ or send a letter to Creative Commons,
PO Box 1866, Mountain View, CA 94042, USA.
"""


class Object:
    def __init__(self):
        # protected variables bind to instance
        self._scene = bpy.context.scene
        self._C = bpy.context
        self._D = bpy.data

        # creating uniq ID
        self._globalCounter = 0

    def selectObject(self, ob):
        """Select via DataID"""
        # Deselect all objects
        self.deselectAll()
        # Make the cube the active object
        self._C.view_layer.objects.active = ob
        ob.select_set(True)
        return ob

    def selectObjectByName(self, name):
        """Select via Name"""
        # Get the object
        ob = self._C.scene.objects[name]
        return self.selectObject(ob)

    def selectObjectinCollection(self, ob, coll):
        """Select object within a Collection via DataID"""
        # Deselect all objects
        self.deselectAll()
        col = bpy.data.collections.get(coll)
        if col:
            for obj in col.objects:
                ob.select_set(True)
        return ob

    def selectObjectinCollectionByName(self, name, coll):
        """Select object within a Collection via Name"""
        # Get the object
        ob = self._C.scene.objects[name]
        return self.selectObjectinCollection(ob, coll)

    def deselectAll(self):
        """Deselect everything"""
        for obj in bpy.data.objects:
            obj.select_set(False)

    def setToOrigin(self, ob):
        """Move ob to 0,0,0"""
        self.selectObject(ob)
        ob.location = (0.0, 0.0, 0.0)

    def duplicate(self, ob):
        """makes a deep copy of the object"""
        template_ob = self.selectObjectByName(ob)
        if template_ob:
            self._globalCounter += 1
            newname = "%s-%s" % (template_ob.name, self._globalCounter)
            ob = bpy.data.objects.new(newname, template_ob.data)
            # ob = template_ob.copy() not a full copy
            return ob
