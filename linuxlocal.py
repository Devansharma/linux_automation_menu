import os
def linuxlocal():
    pass
while True:
    print("\n\nList of linux commands")
    print("\tPress 1 To Know Who You Are??")
    print("\tPress 2 To Check Your System IP")
    print("\tPress 3 To Check Internet Connectivity")
    print("\tPress 4 To Run Date")
    print("\tPress 5 To See Calender")
    print("\tPress 6 To Start Any Service")
    print("\tPress 7 To Copy Any File From Your BaseOS To Another Linux System")
    print("\tPress 8 Want To Reboot Your System?")
    print("\tPress 0 To type the command yourself")
    print("\tPress 10 to go back to prevoius menu")


    ch = input("Enter your Choice :")

    if int(ch)==1:
        os.system("whoami")
    elif int(ch)==2:
        os.system("ifconfig")
    elif int(ch)==3:
        os.system("ping www.google.com")
    elif int(ch)==4:
        os.system("date")
    elif int(ch)==5:
        os.system("cal")
    elif int(ch)==6:
        service = input("Enter The Service!! :")
        choice = input("Want To Start or Stop Service? : ")
        if choice=="start":
            os.system("systemctl start {}".format(service))
            os.system("systemctl status {}".format(service))
        elif choice=="stop":
            os.system("systemctl stop {}".format(service))
            os.system("systemctl status {}".format(service))
    elif int(ch)==7:
        file= input("Enter The File To Be Copied : ")
        ip = input("Enter The IP Address :")
        os.system("scp {file} {ip}:/root ".format(file=file,ip=ip))
    elif int(ch)==8:
        os.system("reboot")
    elif int(ch)==0:
        command = input("Enter the command: ")
        os.system(command)
    elif int(ch)==10:
        from menulocal import localmenu
        break
    else:
        print("Error!!!!\nNo supported action selected \nContact the developer")
