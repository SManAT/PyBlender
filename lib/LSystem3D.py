# -*- coding: utf-8 -*-
"""
Mag. Stefan Hagmann 2020
This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/ or send a letter to Creative Commons,
PO Box 1866, Mountain View, CA 94042, USA.
"""
import math

'''
Represents a Turtel System for a 3D Lindenmayer System
'''
class LSystem3D:
	alpha=90
	axiom=""
	regeln = []

	debug=False
	code=[]
	length=100;
	alphabet=""

	def __init__(self):
		pass

	def output(self, msg):
		if self.debug==True:
			print msg

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

		print "Fertiger Code: %s" % (self.getFinalCode(code))
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
