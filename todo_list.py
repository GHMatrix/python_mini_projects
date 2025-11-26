task = []

try:
	with open("tasks.txt", "r") as file:
		for line in file:
			line = line.strip()
			if line:
				task.append(line)
	except FileNotFoundError:
		#File does not exist yet

		pass
