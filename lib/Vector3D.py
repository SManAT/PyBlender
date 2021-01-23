# -*- coding: utf-8 -*-
import math
"""
Mag. Stefan Hagmann 2020
This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/ or send a letter to Creative Commons,
PO Box 1866, Mountain View, CA 94042, USA.
"""


class Vector(object):
    ''' defines a vector '''
    # hier werden Classen Attribute erstellt

    # imKonstruktor werden Instanz Attribute erstellt
    def __init__(self, x, y, z):
        # A double underscore: Private variable
        # A single underscore: Protected variable
        self._koord = [x, y, z]
        self._name = "vec"

    def getX(self):
        return self._koord[0]

    def getY(self):
        return self._koord[1]

    def getZ(self):
        return self._koord[2]

    def setX(self, x):
        self._koord[0] = x

    def setY(self, y):
        self._koord[1] = y

    def setZ(self, z):
        self._koord[2] = z

    def setName(self, name):
        self._name = name

    def getName(self):
        return self._name

    ''' print out the Vector '''
    def _output(self, dim):
        str = ""
        for i in range(0, dim):
            str += "%s, " % self._koord[i]
        # Delete last Char
        str = str[:-2]
        print("%s > [%s]" % (self._name, str))

    def length(self):
        ''' length of the vector '''
        return math.sqrt(self._koord[0]**2 + self._koord[1]**2 + self._koord[2]**2)

# ------------------------------------------------------------------------------


class Vector3D(Vector):
    ''' represents a 3D Vector '''
    def __init__(self, x, y, z):
        self._koord = [x, y, z]
        self._name = "vec"

    def output(self):
        ''' print out the Vector '''
        self._output(3)

    def add(self, v):
        """ 3D Vector Add """
        self._koord[0] += v.getX()
        self._koord[1] += v.getY()
        self._koord[2] += v.getZ()

    def sub(self, v):
        """ 3D Vector Subtraction """
        self._koord[0] -= v.getX()
        self._koord[1] -= v.getY()
        self._koord[2] -= v.getZ()

    def scalar(self, k):
        """ 3D Vector multiply with an scalar """
        self._koord[0] *= k
        self._koord[1] *= k
        self._koord[2] *= k

    def multiply(self, v):
        return self.scalarProduct(v)

    def scalarProduct(self, v):
        """ 3D Vector Multiplication """
        return self._koord[0] * v.getX() + self._koord[1] * v.getY() + self._koord[2] * v.getZ()

    def length(self):
        """ get length of vector """
        return super().length()

    def unit(self):
        """ make vector length 1 """
        length = self.length()
        self.scalar(1 / length)

    def exProduct(self, v):
        """ calculates the exproduct an return a new Vector """
        ex = Vector3D(0, 0, 0)
        x = self.getY() * v.getZ() - self.getZ() * v.getY()
        y = self.getZ() * v.getX() - self.getX() * v.getZ()
        z = self.getX() * v.getY() - self.getY() * v.getX()
        ex.setX(x)
        ex.setY(y)
        ex.setZ(z)
        return ex

    def createNewVectorObject(self):
        ''' creates a new Object from self '''
        return Vector3D(self.getX(), self.getY(), self.getZ())

    def Tests(self):
        ''' some Tests '''
        # Tests
        v1 = Vector3D(1, 2, 3)
        v2 = Vector3D(-7, 8, 9)

        v1.output()
        v2.output()

        v3 = v1.exProduct(v2)
        v3.output()
