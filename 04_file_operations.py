with open("/home/bogdanc/python/01basics/01file_operations/text01.txt", newline = "") as f:
	lines = f.readlines()

	for line in lines:
		print(line)


with open("/home/bogdanc/python/01basics/01file_operations/text02.txt", "w") as f:
	# the file is open for writing
	for i in range(0, 10, 2):
		f.write(f"This is the line number: {i} \n")
