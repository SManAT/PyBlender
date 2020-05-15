# -*- coding: utf-8 -*-
"""
Mag. Stefan Hagmann 2020
This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/ or send a letter to Creative Commons,
PO Box 1866, Mountain View, CA 94042, USA.
"""
import math

import os
import sys
rootPath = os.path.abspath(os.path.join(os.path.dirname(__file__)))
libPath = os.path.join(rootPath, "./")
# add libPath to SystemPath
sys.path.insert(0, libPath)

from Vector3D import Vector3D
from mathutils import Vector


class LSystem3D:
    '''
    Represents a Turtel System for a 3D Lindenmayer System
    '''
    _regeln = []
    _code = []
    _alphabet = ""
    _posStack = []

    # all pollines
    __polylines = []
    # only one line
    __line = []

    def __init__(self):
        # Heading Vector along x Axis
        self._H = Vector3D(1, 0, 0)
        self._H.setName("Heading")
        # Left Vector along y Axis
        self._L = Vector3D(0, 1, 0)
        self._H.setName("Left")
        # Up Vector along z Axis
        self._U = Vector3D(0, 0, 1)
        self._H.setName("Up")
        # initial Positon = Origin
        self._Pos = Vector3D(0, 0, 0)
        self._H.setName("Pos")
        # initial rotation angle
        self._alpha = 90
        # initial length of moving forward
        self._length = 100
        self._axiom = ""

    def setAlpha(self, w):
        self._alpha = w

    def setAxiom(self, a):
        self._axiom = a

    def setPos(self, x, y, z):
        self._Pos = Vector3D(x, y, z)

    ''' a rule is added '''
    def addRegel(self, regel):
        self._regeln.append(regel)

    ''' remove the alphabet '''
    def getFinalCode(self, code):
        erg = ""
        for char in code:
            if self.is_Alphabet(char) is False:
                erg += char
        return erg

    ''' Prints the final LSystem without Alphabet '''
    def printFinalCode(self):
        print("Final Code: %s" % self.getFinalCode(self._code))

    ''' checks if an character is from alphabet '''
    def is_Alphabet(self, char):
        found = False
        for aChar in self._alphabet:
            if aChar == char:
                found = True
        return found

    ''' iterate '''
    def iterate(self, iterationen):
        code = self._axiom
        if iterationen > 0:
            for i in range(iterationen):
                new_code = ""
                for c in code:
                    # Regeln durcharbeiten
                    replaced = False
                    for k in range(len(self._regeln)):
                        item = self._regeln[k]
                        if c == item[0]:
                            new_code += item[1]
                            replaced = True
                    if replaced is False:
                        # Zeichen übernehmen
                        new_code += c

                code = new_code

        print("Fertiger Code: %s" % (self.getFinalCode(code)))
        self._code = code

    ''' emptys the List and places the first Point into it '''
    def clearPolyLines(self):
        del self.__polylines[:]
        self.__polylines = []
        # store the first point
        self.__line.append(self._Pos)

    ''' clear one single Line data Array '''
    def clearLine(self):
        del self.__line[:]
        self.__line = []

    ''' store the actualPosition to Line Object '''
    def storePos(self):
        # otherwise only references are stored!
        v = self._Pos.createNewVectorObject()
        self.__line.append(v)

    def appendLine(self):
        ''' append line object to polylines list '''
        # if line has only one point, than dismiss
        if len(self.__line) > 1:
            self.__polylines.append(list(self.__line))
        # new line
        self.clearLine()

    '''
    calculate the 3D Points
    return: a array of polylines to Draw
            new polylines are created with
            ] ... pop from stack
            f ... dont draw line
    '''
    def calculate(self):
        # empty the List
        self.clearPolyLines()
        # empty single line Object
        self.clearLine()
        for char in self._code:
            if char == "F":
                # add tp point H vector
                self._Pos.add(self._H)
                self.storePos()

            elif char == "+":
                # left(self.alpha)
                pass

            elif char == "-":
                # right(self.alpha)
                pass

            elif char == "f":
                # single polyline is done, create a new ones
                self.appendLine()
                self._Pos.add(self._H)
                self.storePos()

            elif char == "&":
                self.rotate_around_L(-self._alpha)

            elif char == "^":
                self.rotate_around_L(self._alpha)

            elif char == "\\":
                self.rotate_around_H(self._alpha)

            elif char == "/":
                self.rotate_around_H(-self._alpha)

            elif char == "|":
                self.rotate_around_H(180)

            elif char == "[":
                ''' store the Position and all Vectors '''
                turtle = Turtle(self._P, self._H, self._U, self._L)
                self._posStack.append(turtle)

            elif char == "]":
                ''' get Turtle Data from Stack '''
                turtle = self._posStack.pop()
                # create new Objects otherwise only reference is stored
                self._Pos = turtle.getP().createNewVectorObject()
                self._H = turtle.getH().createNewVectorObject()
                self._U = turtle.getU().createNewVectorObject()
                self._L = turtle.getL().createNewVectorObject()

                # single polyline is done, create a new ones
                self.appendLine()
                self.storePos()

            else:
                # check if constant or alphabet
                if self.is_Alphabet(char):
                    # ist im Alphabet > mach nichts
                    pass
                else:
                    # wird wie F behandelt
                    # forward(self._length)
                    pass

        print(self.__line)
        self.appendLine()
        print(self.__polylines)

    def __Vector2String(self, v):
        ''' the Vector as a string '''
        print(v)
        return "[%s, %s, %s]" % (v.getX(), v.getY(), v.getZ())

    def printPolyLines(self):
        ''' for debugging purpose '''
        print("Vektor List")
        for line in self.__polylines:
            for v in line:
                self.printVector(v)
        print("-END- Vektor List")

    def getPolyLines(self):
        '''
        get the Vectorlist as a List of Vector((x,y,z))
        this is needed in Blender to draw the Polyline
        '''
        erg = []
        single_line = []
        for line in self.__polylines:
            del single_line[:]
            single_line = []
            for v in line:
                # convert to mathutils.Vector()
                single_line.append(Vector((v.getX(), v.getY(), v.getZ())))
            erg.append(single_line)
        return erg

    def output(self):
        ''' print informations '''
        print("Position: %s" % self.__Vector2String(self._Pos))
        print("Heading: %s" % self.__Vector2String(self._H))
        print("Up: %s" % self.__Vector2String(self._U))
        print("Left: %s" % self.__Vector2String(self._L))
        print("Vectors: %s" % len(self.__polylines))
        print("Code Length: %s" % len(self._code))

    def printVector(self, v):
        ''' prints the Vector3D '''
        print("%s" % self.__Vector2String(v))

    def __rotateMatrix(self, alpha, rvec):
        '''
        the main Transformation Matrix to rotate along a vector
        :param double alpha: rotation angle in derees
        :param Vector3D rvec: rotate around this vector
        :return: a matrix
        '''
        rad_alpha = alpha * math.pi / 180
        t = 1 - math.cos(rad_alpha)
        S = math.sin(rad_alpha)
        C = math.cos(rad_alpha)
        matrix = []
        matrix.append([])
        matrix.append([])
        matrix.append([])

        # first Row
        matrix[0].append(t * rvec.getX()**2 + C)
        matrix[0].append(t * rvec.getX() * rvec.getY() - S * rvec.getZ())
        matrix[0].append(t * rvec.getX() * rvec.getZ() + S * rvec.getY())

        # second Row
        matrix[1].append(t * rvec.getX() * rvec.getY() + S * rvec.getZ())
        matrix[1].append(t * rvec.getY()**2 + C)
        matrix[1].append(t * rvec.getY() * rvec.getZ() - S * rvec.getX())

        # third Row
        matrix[2].append(t * rvec.getX() * rvec.getZ() - S * rvec.getY())
        matrix[2].append(t * rvec.getY() * rvec.getZ() + S * rvec.getX())
        matrix[2].append(t * rvec.getZ()**2 + C)

        return matrix

    def __matrixMulVector(self, matrix, v):
        '''
        multiply 3D Vector with matrix
        :return: a Vector3D
        '''
        x = matrix[0][0] * v.getX() + matrix[0][1] * v.getY() + matrix[0][2] * v.getZ()
        y = matrix[1][0] * v.getX() + matrix[1][1] * v.getY() + matrix[1][2] * v.getZ()
        z = matrix[2][0] * v.getX() + matrix[2][1] * v.getY() + matrix[2][2] * v.getZ()
        return Vector3D(x, y, z)

    def rotate_around_H(self, alpha):
        ''' rotates along the Head Vector '''
        matrix = self.__rotateMatrix(alpha, self._H)
        Up = self.__matrixMulVector(matrix, self._U)
        Left = self.__matrixMulVector(matrix, self._L)
        self._U = Up
        self._L = Left

    def rotate_around_U(self, alpha):
        ''' rotates along the Up Vector '''
        matrix = self.__rotateMatrix(alpha, self._U)
        Heading = self.__matrixMulVector(matrix, self._H)
        Left = self.__matrixMulVector(matrix, self._L)
        self._H = Heading
        self._L = Left

    def rotate_around_L(self, alpha):
        ''' rotates along the L Vector '''
        matrix = self.__rotateMatrix(alpha, self._L)
        Up = self.__matrixMulVector(matrix, self._U)
        Heading = self.__matrixMulVector(matrix, self._H)
        self._U = Up
        self._H = Heading

    def Test(self):
        ''' some Testing  '''
        # Draw a equilateral triangle
        print("---------------------------------------------------------------")
        self._alpha = 120
        self.rotate_around_H(45)
        self.output()
        self._code = "F&F&FffF&F&F"
        self._code = "FFffFF"
        self.calculate()
        # self.printPolyLines()

# ------------------------------------------------------------------------------


class Turtle:
    '''
    Stores all data for the Turtle
    Pos, H, L, U etc
    '''
    def __init__(self, P, H, U, L):
        self.__Pos = P.createNewVectorObject()
        self.__H = H.createNewVectorObject()
        self.__U = U.createNewVectorObject()
        self.__L = L.createNewVectorObject()

    def getH(self):
        return self.__H

    def getU(self):
        return self.__U

    def getP(self):
        return self.__P

    def getL(self):
        return self.__L


LSys = LSystem3D()
LSys.Test()
'''

LSys._alpha = 120
LSys.rotate_around_H(45)
LSys._code = "F&F&F"
LSys.calculate()
LSys.printPolyLines()
LSys.setPos(0, 0, 0)
LSys.setAlpha(90)
LSys.setAxiom("X")
regel = ["X", "^\XF^\XFX-F^//XFX&F+//XFX-F/X-/"]
LSys.addRegel(regel)
LSys.iterate(2)
'''
