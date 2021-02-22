import bpy
import math

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

    def translate(self, ob, deltax, deltay, deltaz):
        """
        Translate the object ob
        :param deltax: x + deltax
        :param deltax: y + deltay
        :param deltax: z + deltaz
        """
        self._D.objects[ob.name].location.x += deltax
        self._D.objects[ob.name].location.y += deltay
        self._D.objects[ob.name].location.z += deltaz

    def rotate(self, ob, alpha, axis):
        """
        Rotate the object ob
        :param alpha: alpha in degrees
        :param axis: the axis, x, y or z Global
        """
        # set the active object
        self._C.view_layer.objects.active = ob
        if axis.lower() == 'x':
            self._D.objects[ob.name].rotation_euler[0] = math.radians(alpha)
        if axis.lower() == 'y':
            self._D.objects[ob.name].rotation_euler[1] = math.radians(alpha)
        if axis.lower() == 'z':
            self._D.objects[ob.name].rotation_euler[2] = math.radians(alpha)

    def rotateSelected(self, alpha, axis):
        """
        Rotate the selected objects
        :param alpha: alpha in degrees
        :param axis: the axis, x, y or z Global
        """
        # set the active object
        if axis.lower() == 'x':
            bpy.ops.transform.rotate(
                value=math.radians(alpha), orient_axis='X', orient_type='GLOBAL'
            )
        if axis.lower() == 'y':
            bpy.ops.transform.rotate(
                value=math.radians(alpha), orient_axis='Y', orient_type='GLOBAL'
            )
        if axis.lower() == 'z':
            bpy.ops.transform.rotate(
                value=math.radians(alpha), orient_axis='Z', orient_type='GLOBAL'
            )

    def scale(self, ob, fact):
        """
        Scale the object ob
        :param fact: the scale factor
        """
        self._D.objects[ob.name].scale = (fact, fact, fact)

    def selectObject(self, ob):
        """
        Select via DataID
        """
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
        objectToSelect = self._D.objects[name]
        objectToSelect.select_set(True)
        self._C.view_layer.objects.active = objectToSelect
        return self.selectObject(ob)

    def selectMultipleRegEX(self, pattern):
        """
        Select multiple Object per patern
        e.g. pattern = Cube
        """
        # Deselect all objects
        for o in self._D.objects:
            if pattern in o.name:
                o.select_set(True)

    def selectObjectinCollection(self, ob, coll):
        """Select object within a Collection via DataID"""
        # Deselect all objects
        self.deselectAll()
        col = self._D.collections.get(coll)
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
        for obj in self._D.objects:
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
            ob = self._D.objects.new(newname, template_ob.data)
            # ob = template_ob.copy() not a full copy
            return ob

    def getDimensions(self, obj):
        """ get Dimensions of object """
        return obj.dimensions

    def getAllAttributes(self, obj):
        """ get the attributes from the object """
        attrs = dir(obj)
        for item in attrs:
            print(item)

    def getVertices(self, obj):
        """ get all vertices from the object """
        return obj.data.vertices
