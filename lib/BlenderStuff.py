import bpy

"""
Mag. Stefan Hagmann 2020
This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/ or send a letter to Creative Commons,
PO Box 1866, Mountain View, CA 94042, USA.
"""


class BlenderStuff:
	def __init__(self):
		# protected variables bind to instance
		self._myScene = bpy.context.scene
		self._C = bpy.context
		self._D = bpy.data

	'''
	Search and remove collection
	'''
	def remove_Collection(self, col_name):
		remove_collection_objects = True
		coll = bpy.data.collections.get(col_name)
		# found
		if coll:
			if remove_collection_objects:
				obs = [o for o in coll.objects if o.users == 1]
				while obs:
					bpy.data.objects.remove(obs.pop())
			bpy.data.collections.remove(coll)

	'''
	Create new collection and add it to scene
	'''
	def create_Collection(self, col_name):
		# first remove old ones
		self.remove_Collection(col_name)
		collection = self._D.collections.new(name=col_name)
		# Add collection to scene
		self._myScene.collection.children.link(collection)
		return collection

	'''
	creates a PolyLine from a list of 3D Vectors and adds it
	to Collection coll
	'''
	def MakePolyLine(self, objname, curvename, cList, coll):
		# weight
		w = 1
		# 'POLY', 'BEZIER', 'BSPLINE', 'CARDINAL', 'NURBS'
		curvedata = self._D.curves.new(name=curvename, type='CURVE')
		curvedata.dimensions = '3D'

		objectdata = self._D.objects.new(objname, curvedata)
		# object origin
		objectdata.location = (0, 0, 0)

		polyline = curvedata.splines.new('POLY')
		polyline.points.add(len(cList) - 1)
		for num in range(len(cList)):
			x, y, z = cList[num]
			polyline.points[num].co = (x, y, z, w)

		# Remove object from Scene Collection
		bpy.ops.collection.objects_remove_all()

		# add it to our specific collection
		self._D.collections[coll].objects.link(objectdata)
