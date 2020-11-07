import os

def dockerssh():
    pass
os.system("clear")

print("Welcome to docker via ssh")
ip = input("Enter the IP you want to connect: ")

while True:
    print("\n\nList of Docker command available:")
    print("\tPress 1 to launch os")
    print("\tPress 2 to see the launched containers")
    print("\tPress 3 to see the downloaded all os images")
    print("\tPress 4 to delete the os")
    print("\tPress 5 to delete the os image")
    print("\tPress 0 to type the command yourself")
    print("\tPress 10 to go back to main menu") 
    cmd = int(input("Enter your choice: "))
    if(cmd == 1):
        name = input("Enter which OS you want to launch: ")
        osn = input("Enter name of the OS: ")
        version = input("Enter the version of OS: ")
        os.system("ssh {0} docker run -it --name {1} {2}:{3}".format(ip,name,osn,version))
    elif(cmd == 2):
        os.system("ssh {0} docker ps".format(ip))
    elif(cmd == 3):
        os.system("ssh {0} docker images".format(ip))
    elif(cmd == 4):
        rep = input("Do you want to delete all the os launched till date (y/n): ")
        if(rep=="y"):
            os.system("ssh {0} docker rm `docker ps -a -q`".format(ip))
        else:
            osname=input("Enter the os name/container id: ")
            os.system("ssh {0} docker rm {1}".format(ip,osname))
    elif(cmd==5):
        osname = input("Enter the name of OS image: ")
        version = input("Enter the version of os")
        os.system("ssh {0} docker rmi -f {1}:{2}".format(ip,osname,version))
    elif(cmd == 0):
        command = input("Enter the command: ")
        os.system("ssh {0} {1}".format(ip,command))
    elif(cmd == 10):
        from menussh import sshmenu
        break
    else:
        print("Error!!!!\nNo supported action selected \nContact the developer")
