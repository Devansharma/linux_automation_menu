import os

def dockerlocal():
    pass
os.system("clear")
while True:
    print("\t\t\tWelcome to Docker")
    print("\n\nList of Hadoop command available:")
    print("\tPress 1 to launch os")
    print("\tPress 2 to see the launched containers")
    print("\tPress 3 to see the downloaded all os images")
    print("\tPress 4 to delete the os")
    print("\tPress 5 to delete the os image")
    print("\tPress 0 to type the command yourself")
    print("\tPress 10 to go back to main menu")
    cmd = int(input("Enter your choice: "))
    if (cmd == 1):
        name = input("Enter which OS you want to launch: ")
        osn = input("Enter name of the OS: ")
        version = input("Enter the version of OS: ")
        os.system("docker run -it --name {0} {1}:{2}".format(name, osn, version))
    elif(cmd == 2):
        os.system("docker ps")
    elif(cmd == 3):
        os.system("docker images")
    elif(cmd == 4):
        rep = input("Do you want to delete all the os launched till date (y/n): ")
        if (rep == "y"):
            os.system("docker rm `docker ps -a -q`")
        else :
            osname = input("Enter the os name/container id: ")
            os.system("docker rm {0}".format(osname))
    elif(cmd == 5):
        osname = input("Enter the name of OS image: ")
        version = input("Enter the version of os")
        os.system("docker rmi -f {0}:{1}".format(osname, version))
    elif(cmd == 0):
        command = input("Enter the command: ")
        os.system(command)
    elif(cmd == 10):
        from menulocal import localmenu
        break
    else :
        print("Error!!!!\nNo supported action selected \nContact the developer")
