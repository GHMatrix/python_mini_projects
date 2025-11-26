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

def show_menu():
	print("\n --- TO-DO LIST ---")
	print("1. View Tasks")
	print("2. Add Task")
	print("3. Delete Task")
	print("4. Mark Task As Done")
	print("5. Exit")
