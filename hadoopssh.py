import os
def hadoopssh():
	pass

print("\t\t\tWelcome to Hadoop via ssh")
ip = input("Type the ip you want to run Hadoop on: ")
while True:
	print("\n\nList of Hadoop command available:")
	print("\tPress 1 to start the name node service")
	print("\tPress 2 to start the data node service")
	print("\tPress 3 to see the running java processes")
	print("\tPress 4 to view the hadoop cluster report")
	print("\tPress 0 to type the command yourself")
	print("\tPress 10 to go back to main menu")
	cmd = int(input("Enter your choice: "))
	if(cmd == 1):
		print("Starting Name Node......")
		os.system("ssh "+ip+" hadoop-daemon.sh start namenode")
		print("Name Node started")
	elif(cmd == 2):
		print("Starting Data Node......")
		os.system("ssh "+ip+" hadoop-daemon.sh start datanode")
		print("Data Node started")
	elif(cmd == 3):
		print("\t\t\tRunning java processes")
		os.system("ssh "+ip+" jps")
	elif(cmd == 4):
		rep = input("Do you want the report in brief? (y/n): ")
		if(rep=="y"):
			os.system("ssh "+ip+" hadoop dfsadmin -report | less")
		else:
			os.system("ssh "+ip+" hadoop dfsadmin -report")
	elif(cmd == 0):
		command = input("Enter the command: ")
		os.system(command)
	elif(cmd == 10):
		from menussh import sshmenu
		break
	else:
		print("Error!!!!\nNo supported action selected \nContact the developer")

