#/usr/bin/python3
# coding: utf-8

import re

class Equation:
	"""Class that store an polynomial equation from a string"""

	monome_pattern = re.compile('[+-]?[ ]*[0-9]*[.,]?[0-9]*[ ]*\\*[ ]*X[ ]*\\^[ ]*[0-9]*')
	coeff_pattern = re.compile('[+-]?[ ]*[0-9]*[.,]?[0-9]*')

	def __init__(self, equation):
		sides = equation.split("=")
		if len(sides) is not 2:
			print("that s not a valid equation")
			exit(1)
		self.left = Equation.to_monomes(Equation.monome_pattern.findall(sides[0]))
		self.right = Equation.to_monomes(Equation.monome_pattern.findall(sides[1]))
		self.degree = int(max(max(self.right.keys()), max(self.left.keys())))
		self.reduce()

	def __str__(self):
		return(
			"Reduced form: {0} = 0\nPolynomial degree: {1}".format(self.reduced_to_human(), self.degree))

	@classmethod
	def to_monomes(cls, raw_monomes):
		monomes = {}
		for monome in raw_monomes:
			try:
				splitted = monome.split("^")
				degree = splitted[1]
				coeff = float(Equation.coeff_pattern.match(splitted[0]).group(0).replace(" ", ""))
				monomes[degree] = coeff
			except ValueError:
				print("Monome {} mal formaté".format(monome))
				exit(1)
		return(monomes)

	def reduced_to_human(self):
		display = ""
		index = 0
		for key in sorted(self.reduced.keys(), reverse=True):
			if index is not 0:
				display += " + " if self.reduced[key] >= 0 else " - " 
			else:
				display += "-" if self.reduced[key] < 0 else ""

			display += "{0} * X^{1}".format(abs(self.reduced[key]), key)
			index += 1
		return (display)

	def reduce(self):
		self.reduced = {}
		for i in range(0, self.degree + 1):
			i = str(i)
			self.reduced[i] = (self.left.get(i) or 0.0) - (self.right.get(i) or 0.0)

