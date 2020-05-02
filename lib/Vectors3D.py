# -*- coding: utf-8 -*-
import math
"""
Mag. Stefan Hagmann 2020
This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/ or send a letter to Creative Commons,
PO Box 1866, Mountain View, CA 94042, USA.
"""

''' defines a vector '''
class Vector(object):
    #hier werden Classen Attribute erstellt

    #imKonstruktor werden Instanz Attribute erstellt
    def __init__(self, x, y, z):
        #A double underscore: Private variable
        #A single underscore: Protected variable
        self._koord = [x,y,z]
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
        str=""
        for i in range(0, dim):
            str += "%s, " % self._koord[i]
        #Delete last Char
        str = str[:-2]
        print("%s > [%s]" % (self._name, str))

    ''' length of the vector '''
    def length(self):
        return math.sqrt(
            self._koord[0]*self._koord[0] +
            self._koord[1]*self._koord[1] +
            self._koord[2]*self._koord[2]
            )

#-------------------------------------------------------------------------------

''' represents a 3D Vector '''
class Vector3D(Vector):
    def __init__(self, x, y, z):
        self._koord = [x,y,z]
        self._name = "vec"

    def output(self):
        ''' print out the Vector '''
        self._output(3)

    def add(self, v2):
        """ 3D Vector Add """
        self._koord[0] += v2.getX()
        self._koord[1] += v2.getY()
        self._koord[2] += v2.getZ()

#-------------------------------------------------------------------------------

''' represents a 2D Vector '''
class Vector2D(Vector):
    def __init__(self, x, y):
        self._koord = [x,y,0]
        self._name = "vec"

    def createVector(self, P1, P2):
        '''
        create a vector between 2 Points, P2 -P1
        Point = Array e.g. [2,-4]
        '''
        self._koord[0] = P2[0] - P1[0]
        self._koord[1] = P2[1] - P1[1]

    def output(self):
        ''' print out the Vector '''
        self._output(2)

    def add(self, v2):
        """ 2D Vector Add """
        self._koord[0] += v2.getX()
        self._koord[1] += v2.getY()

    def sub(self, v2):
        """ 2D Vector Sub """
        self._koord[0] -= v2.getX()
        self._koord[1] -= v2.getY()

    def scalar(self, k):
        """ 2D Vector multiply with scalar """
        self._koord[0] *= k
        self._koord[1] *= k

    def length(self):
        """ get length of vector """
        return super().length()

    def unit(self):
        """ make vector length 1 """
        l = self.length()
        self.scalar(1/l)

    def scalarProduct(self, v):
        """ calculate the scalar Product """
        return self._koord[0] * v.getX() + self._koord[1] * v.getY()


    def getAngle(self, v):
        """ get the angle from vector between self and v """
        c = self.scalarProduct(v) / self.length() / v.length()
        return math.acos(c)*180/math.pi
