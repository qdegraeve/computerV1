#/usr/bin/python3
# coding: utf-8

import re

def sqrt_root(number):
    if(number == 0):
        return 0;

    g = number/2.0;
    g2 = g + 1;
    while(g != g2):
        n = number/ g;
        g2 = g;
        g = (g + n)/2;

    return g;

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
		if self.degree <= 2:
			self.find_discriminant()

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

	def a(self):
		return(self.reduced.get('2') or 0)

	def b(self):
		return(self.reduced.get('1') or 0)

	def c(self):
		return(self.reduced.get('0') or 0)

	def find_discriminant(self):
		self.discriminant = (self.b() * self.b()) - (4 * self.a() * self.c())

	def solutions(self):
		if self.degree > 2:
			print("The polynomial degree is stricly greater than 2, I can't solve.")
		else:
			if self.degree < 2 or self.discriminant is 0:
				print("The solution is:")
				self.simple_solution()
			elif self.discriminant > 0:
				print("Discriminant is strictly positive, the two solutions are:")
				self.solution1()
				self.solution2()
			else:
				print("Discriminant is strictly negative, there is no solution")

	def simple_solution(self):
		if self.degree is 0:
			return(print(self.c()))
		if self.discriminant is 2:
			self.solution1
		else:
			print(- self.c() / self.b())

	def solution1(self):
		print((- self.b() + (sqrt_root(self.discriminant))) / (2 * self.a()))

	def solution2(self):
		print((- self.b() - (sqrt_root(self.discriminant))) / (2 * self.a()))

	def reduce(self):
		self.reduced = {}
		for i in range(0, self.degree + 1):
			i = str(i)
			self.reduced[i] = (self.left.get(i) or 0.0) - (self.right.get(i) or 0.0)

