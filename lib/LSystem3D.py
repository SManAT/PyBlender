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
#add libPath to SystemPath
sys.path.insert(0, libPath)

from Vector3D import Vector3D

'''
Represents a Turtel System for a 3D Lindenmayer System
'''
class LSystem3D:
    axiom=""
    regeln = []

    code=[]
    length=100;
    alphabet=""

    def __init__(self):
        #Heading Vector along x Axis
        self._H = Vector3D(1,0,0)
        self._H.setName("Heading")
        #Left Vector along y Axis
        self._L = Vector3D(0, 1, 0)
        self._H.setName("Left")
        #Up Vector along z Axis
        self._U = Vector3D(0, 0, 1)
        self._H.setName("Up")
        #initial Positon = Origin
        self._Pos = Vector3D(0,0,0)
        self._H.setName("Pos")
        #initial rotation angle
        self._alpha=90
        pass

    ''' a rule is added '''
    def addRegel(self, regel):
        self.regeln.append(regel)

    ''' remove the alphabet '''
    def getFinalCode(self, code):
        erg=""
        for char in code:
            if self.is_Alphabet(char)==False:
                erg += char
        return erg

    ''' checks if an character is from alphabet '''
    def is_Alphabet(self, char):
        found = False
        for aChar in self.alphabet:
            if aChar==char:
                found=True
        return found

    ''' iterate '''
    def iterate(self, iterationen):
        ht()
        code = self.axiom
        if iterationen>0:
            for i in range(iterationen):
                new_code = ""
                for c in code:
                    #Regeln durcharbeiten
                    replaced=False
                    for k in range(len(self.regeln)):
                        item = self.regeln[k]
                        if c==item[0]:
                            new_code += item[1]
                            replaced=True
                    if replaced==False:
                        #Zeichen übernehmen
                        new_code += c

                code = new_code
                self.output(code)

        print("Fertiger Code: %s" % (self.getFinalCode(code)))
        self.code = code
        st()

    ''' calculate the 3D Points '''
    def draw(self):
        for char in self.code:
            if char=="F":
                forward(self.length)

            elif char=="+":
                left(self.alpha)

            elif char=="-":
                right(self.alpha)

            elif char=="f":
                pu()
                forward(self.length)
                pd()
            else:
                #check if constant or alphabet
                if self.is_Alphabet(char):
                    #ist im Alphabet > mach nichts
                    pass
                else:
                    #wird wie F behandelt
                    forward(self.length)

    def __Vector2String(self, v):
        return "[%s, %s, %s]" % (v.getX(), v.getY(), v.getZ())


    def output(self):
        ''' print information s '''
        print("Position: %s" % self.__Vector2String(self._Pos))
        print("Heading: %s" % self.__Vector2String(self._H))
        print("Up: %s" % self.__Vector2String(self._U))
        print("Left: %s" % self.__Vector2String(self._L))


    def __rotateMatrix(self, alpha, rvec):
        '''
        the main Transformation Matrix to rotate along a vector
        :param double alpha: rotation angle in derees
        :param Vector3D rvec: rotate around this vector
        :return: a matrix
        '''
        rad_alpha = alpha * math.pi /180
        t = 1 - math.cos(rad_alpha)
        S = math.sin(rad_alpha)
        C = math.cos(rad_alpha)
        matrix = []
        matrix.append([])
        matrix.append([])
        matrix.append([])

        #first Row
        matrix[0].append( t*rvec.getX()**2 + C )
        matrix[0].append( t*rvec.getX()*rvec.getY() - S*rvec.getZ() )
        matrix[0].append( t*rvec.getX()*rvec.getZ() + S*rvec.getY() )

        #second Row
        matrix[1].append( t*rvec.getX()*rvec.getY() + S*rvec.getZ() )
        matrix[1].append( t*rvec.getY()**2 + C )
        matrix[1].append( t*rvec.getY()*rvec.getZ() - S*rvec.getX() )

        #third Row
        matrix[2].append( t*rvec.getX()*rvec.getZ() - S*rvec.getY() )
        matrix[2].append( t*rvec.getY()*rvec.getZ() + S*rvec.getX() )
        matrix[2].append( t*rvec.getZ()**2 + C )

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
        LSys = LSystem3D()
        LSys.output()
        LSys.rotate_around_H(30)
        LSys.output()
