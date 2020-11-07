import os

def localmenu():
	pass
while True:
    os.system("tput setaf 3")
    print("\n\nPress 1 to use hadoop")
    print("Press 2 to use docker")
    print("Press 3 to use linux")
    print("Press 4 to use the disk management tools")
    print("Press 0 to exit")
    os.system("tput setaf 7")
    prog = int(input("Enter your choice: "))
    if(prog==1):
        from hadooplocal import hadooplocal
    elif(prog==2):
        from dockerlocal import dockerlocal
    elif(prog==3):
        from linuxlocal import linuxlocal
    elif(prog==4):
        from lvmlocal import lvmlocal
    elif(prog==0):
        break
    else:
        print("Error!!!!\nNo supported action selected \nContact the developer")
