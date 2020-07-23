import bpy

"""
Mag. Stefan Hagmann 2020
This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/ or send a letter to Creative Commons,
PO Box 1866, Mountain View, CA 94042, USA.
"""


class Collection:
    def __init__(self):
        # protected variables bind to instance
        self._scene = bpy.context.scene
        self._C = bpy.context
        self._D = bpy.data

    def remove_Collection(self, col_name):
        """Search and remove collection"""
        remove_collection_objects = True
        coll = bpy.data.collections.get(col_name)
        # found
        if coll:
            if remove_collection_objects:
                obs = [o for o in coll.objects if o.users == 1]
                while obs:
                    bpy.data.objects.remove(obs.pop())
            bpy.data.collections.remove(coll)

    def create_Collection(self, col_name):
        """Create new collection and add it to scene"""
        # first remove old ones
        self.remove_Collection(col_name)
        collection = self._D.collections.new(name=col_name)
        # Add collection to scene
        self._scene.collection.children.link(collection)
        return collection

    def add_to_Collection(self, objectdata, col_name):
        """Add something to a collection."""
        self._D.collections[col_name].objects.link(objectdata)

    def remove_from_Collection(self, objectdata, col_name):
        """Remove something from a collection."""
        self._D.collections[col_name].objects.unlink(objectdata)

    def move_to_Collection(self, obj, col1, col2):
        """Move Object from col1 to col2"""
        # put the obj in the new collection
        c1 = self._D.collections[col1]
        c2 = self._D.collections[col2]
        c2.objects.link(obj)
        # remove it from the old collection
        c1.objects.unlink(obj)

    def get_obj_collection(name):
        """determin collection in where the obj is"""
        item = bpy.data.objects[name]
        collections = item.users_collection
        if len(collections) > 0:
            return collections[0]
        return bpy.contex.scene.collection
