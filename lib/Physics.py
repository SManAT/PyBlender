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
            bpy.context.object.modifiers["Softbody"]
            return True
        except KeyError:
            return False

    def _setKey(self, obj, key):
        """ sets a Key for an object"""
        bpy.context.view_layer.objects.active = obj
        if key == "Softbody":
            bpy.ops.object.modifier_add(type='SOFT_BODY')

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
