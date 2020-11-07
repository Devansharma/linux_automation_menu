import os

def sshmenu():
	pass
while True:
    os.system("tput setaf 3")
    print("\t\t\tSelect the program to run via ssh")
    print("\n\nPress 1 to use hadoop")
    print("Press 2 to use docker")
    print("Press 3 to use linux")
    print("Press 4 to use the disk management tools")
    print("Press 0 to exit")
    os.system("tput setaf 7")
    prog = int(input("Enter your choice: "))
    if(prog==1):
        from hadoopssh import hadoopssh
    elif(prog==2):
        from dockerssh import dockerssh
    elif(prog==3):
        from linuxssh import linuxssh
    elif(prog==4):
        from lvmssh import lvmssh
    elif(prog==0):
        break
    else:
        print("Error!!!!\nNo supported action selected \nContact the developer")

