"""
3. Dancing Parabolas

Write a function or program that will calculate the zeros of the given square
function.
"""

from math import sqrt

def read_parameters():
	print("Insert the coefficients for a second degree equation - parabola \
		\n ax^2 + bx + c = 0 ")
	a = int(input("a = "))
	b = int(input("b = "))
	c = int(input("c = "))
	print(f"You inserted the equation: \n \
		{a}x^2 + {b}x + {c}")
	return a, b, c

def calculate_zeros():
	a, b, c = read_parameters()
	if b == 0:
		return sqrt(-c / a)
	delta  = b * b - 4 * a * c
	if delta < 0:
		print("Insert a new set of coefficients")
		a, b, c = read_parameters()
	elif delta == 0:
		return (-b / (4 * a * c)), (b / (4 * a * c))
	else:
		return ((-b - sqrt(delta)) / (2 * a)), \
		((-b + sqrt(delta)) / (2 * a))

while(True):
	print(79 * "-")
	print("Input 1 to continue.")
	print("Input 2 to exit.")
	print(79 * "-")

	access = int(input("Option:  "))
	print(f"Selected: {access}")
	
	if access == 2:
		print("Exiting", 79 * "-", sep = "\n")
		break

	elif access == 1:
		results = calculate_zeros()
		print("The solutions are:")
		i = 1
		for result in results:
			print(f"x{i} = {result}")
			i += 1

	else:
		print(79 * "-", "Please select 1 or 2", 79 * "-", sep = "\n")
		continue