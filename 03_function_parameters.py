# add any number of arguments
def add_ingredients(*args, **kwargs):
	result = 0
	for arg in args:
		result += arg
	for key in kwargs:
		result += kwargs[key]
	return result

print(add_ingredients(1, 2, 3, eggs = 3, spam = 5, cheese = 2)) # return 16
