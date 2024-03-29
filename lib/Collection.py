import bpy

"""
Mag. Stefan Hagmann 2020
This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/ or send a letter to Creative Commons,
PO Box 1866, Mountain View, CA 94042, USA.
"""


class Collection:

    def remove_Collection(self, col_name):
        """Search and remove collection"""
        remove_collection_objects = True
        coll = bpy.data.collections.get(col_name)
        # found
        if coll:
            if remove_collection_objects:
                obs = [o for o in coll.objects if o.users == 1]
                while obs:
                    bpy.data.objects.remove(obs.pop(), do_unlink=True)
            bpy.data.collections.remove(coll)

        # Clean Up orphaned Meshes !! Important sont wird die Datei immer größer
        for m in bpy.data.meshes:
            found = False
            
            # search in all Collections
            for collection in bpy.data.collections:
                for obj in collection.all_objects:
                    # jedes objekt hat auch ein Mesh Data mit Namen
                    if obj.data:
                        #print("obj: ", obj.data.name)
                        if obj.data.name == m.name:
                            found = True
                            break
                if found:
                    break
            if found is False:
                # delete orphaned Mesh
                # print(f"CleanUp orphaned Mesh {m.name}")
                bpy.data.meshes.remove(m)
        print("Cleaning orphaned Meshes done ...")

    def create_Collection(self, col_name):
        """Create new collection and add it to scene"""
        # first remove old ones
        self.remove_Collection(col_name)
        collection = bpy.data.collections.new(name=col_name)
        # Add collection to scene
        bpy.context.scene.collection.children.link(collection)
        return collection

    def add_to_Collection(self, objectdata, col_name):
        """Add something to a collection."""
        bpy.data.collections[col_name].objects.link(objectdata)

    def remove_from_Collection(self, objectdata, col_name):
        """Remove something from a collection."""
        bpy.data.collections[col_name].objects.remove(objectdata, do_unlink=True)

    def move_to_Collection(self, obj, col1, col2):
        """Move Object from col1 to col2"""
        # put the obj in the new collection
        c1 = bpy.data.collections[col1]
        c2 = bpy.data.collections[col2]
        c2.objects.link(obj)
        # remove it from the old collection
        c1.objects.unlink(obj)

    def get_obj_collection(self, name):
        """determin collection in where the obj is"""
        item = bpy.data.objects[name]
        collections = item.users_collection
        if len(collections) > 0:
            return collections[0]
        return bpy.contex.scene.collection

    def selectAllInCollection(self, name):
        """ select all Objects within a collection """
        for obj in bpy.data.collections[name].all_objects:
            obj.select_set(True)

    def setActiveCollection(self, name):
      """ set the active used collection """
      bpy.context.view_layer.active_layer_collection = bpy.context.view_layer.layer_collection.children[name]
