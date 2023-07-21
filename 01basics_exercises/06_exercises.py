"""
2. Write a program to determine if a number is preceeded by a prime number.
"""

from math import sqrt

def previous_is_prime(some_number):
	the_number = some_number - 1
	for i in range(2, int(sqrt(the_number + 1))):
		if the_number % i == 0:
			return False
	return True

my_num = 1
while(my_num != 0):
	my_num = int(input("Input 0 to exit or: \n Insert a number: "))
	if my_num == 0:
		print("Exiting!")
		break
	if my_num < 2:
		print(f"Insert a number greater than 2.")
		continue
	if previous_is_prime(my_num):
		print(f"The number {my_num} is preceeded by a prime {my_num - 1}")
	else:
		print(f"The number {my_num} is not preceeded by a prime: {my_num - 1}")
