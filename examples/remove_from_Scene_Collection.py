context = bpy.context
scene = context.scene

for c in scene.collection.children:
    scene.collection.children.unlink(c)
