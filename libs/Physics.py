import bpy

"""
Mag. Stefan Hagmann 2020
This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/ or send a letter to Creative Commons,
PO Box 1866, Mountain View, CA 94042, USA.
"""


class Physics:
    def __init__(self):
        pass

    def _hasKey(self, obj, key):
        """ test if obj has such a Key """
        bpy.context.view_layer.objects.active = obj
        try:
            bpy.context.object.modifiers[key]
            return True
        except KeyError:
            return False

    def _setKey(self, obj, key):
        """ sets a Key for an object"""
        bpy.context.view_layer.objects.active = obj
        if key == "Softbody":
            bpy.ops.object.modifier_add(type='SOFT_BODY')
        if key == "Collision":
            bpy.ops.object.modifier_add(type='COLLISION')
        if key == "Subdivision":    
            bpy.ops.object.modifier_add(type='SUBSURF')


    def copySoftBody(self, source, target):
        """ Copy soft body settings from source to target """
        bpy.context.view_layer.objects.active = source
        src = bpy.context.object.modifiers["Softbody"].settings

        # set missing Key if not exists
        if self._hasKey(target, "Softbody") is False:
            self._setKey(target, "Softbody")

        bpy.context.view_layer.objects.active = target
        tgt = bpy.context.object.modifiers["Softbody"].settings

        for attr in dir(src):
            if attr == 'effector_weights':
                for item in dir(src.effector_weights):
                    if not attr.startswith('__'):
                        try:
                            setattr(tgt.effector_weights, item, getattr(src.effector_weights, item))
                        except Exception:
                            pass
            elif not attr.startswith('__'):
                try:
                    setattr(tgt, attr, getattr(src, attr))
                except Exception:
                    pass

        # copy Cache settings
        bpy.context.view_layer.objects.active = source
        src = bpy.context.object.modifiers["Softbody"].point_cache
        bpy.context.view_layer.objects.active = target
        tgt = bpy.context.object.modifiers["Softbody"].point_cache
        for attr in dir(src):
            try:
                setattr(tgt, attr, getattr(src, attr))
            except Exception:
                pass
                    
    def copyCollision(self, source, target):
        """ Copy soft body settings from source to target """
        bpy.context.view_layer.objects.active = source
        src = bpy.context.object.modifiers["Collision"].settings
        # set missing Key if not exists
        if self._hasKey(target, "Collision") is False:
            self._setKey(target, "Collision")

        bpy.context.view_layer.objects.active = target
        tgt = bpy.context.object.modifiers["Collision"].settings

        for attr in dir(src):
            try:
                setattr(tgt, attr, getattr(src, attr))
            except Exception:
                pass
                
    def copySubdivision(self, source, target):
        """ Copy Subdivision Modifier from Source to Target """
        bpy.context.view_layer.objects.active = source
        src = bpy.context.object.modifiers["Subdivision"]
        
        # set missing Key if not exists
        if self._hasKey(target, "Subdivision") is False:
            self._setKey(target, "Subdivision")

        bpy.context.view_layer.objects.active = target
        tgt = bpy.context.object.modifiers["Subdivision"]

        for attr in dir(src):
            try:
                setattr(tgt, attr, getattr(src, attr))
            except Exception:
                pass


    def copyAllModifiers(self, src, target):
        """ get all Modifiers from src and apply them an target """
        self.copySoftBody(src, target)
        self.copyCollision(src, target)
        self.copySubdivision(src, target) 
