import os

def linuxssh():
    pass

print("\t\t\tWelocome to LVM via ssh")
ip = input("Type the IP you want to run LVM on: ")

while True:
    print("""
    \n
    Press 1 To Know Who You Are??
        Press 2 To Check Your System IP
        Press 3 To Check Internet Connectivity
        Press 4 To Run Date
        Press 5 To See Calender
        Press 6 To Start Any Service
        Press 7 To Copy Any File From Your BaseOS To Another Linux System
        Press 8 Want To Reboot Your System?
        Press 0 To type the command yourself
        Press 10 to go back to prevoius menu
        """)
    ch = input("Enter your Choice :")

    if int(ch)==1:
        os.system("ssh {} whoami".format(ip))
    elif int(ch)==2:
        os.system("ssh {} ifconfig".format(ip))
    elif int(ch)==3:
        os.system("ssh {} ping www.google.com".format(ip))
    elif int(ch)==4:
        os.system("ssh {} date".format(ip))
    elif int(ch)==5:
        os.system("ssh {} cal".format(ip))
    elif int(ch)==6:
        service = input("Enter The Service!! :")
        choice = input("Want To Start or Stop Service? :")
        if choice=="start":
            os.system("ssh {ip} systemctl start {service}".format(ip=ip,service=service))
            os.system("ssh {ip} systemctl status {service}".format(ip=ip,service=service))
        if choice=="stop":
            os.system("ssh {ip} systemctl stop {service}".format(ip=ip,service=service))
            os.system("ssh {ip} systemctl status {service}".format(ip=ip,service=service))
    elif int(ch)==7:
        file= input("Enter The File To Be Copied :")
        print(file)
        ips = input("Enter The IP Address :")
        print(ip)
        os.system("ssh {ip} python3/root/{file}".format(ip=ips,file=file))
    elif int(ch)==8:
        os.system("ssh {} reboot".format(ip))
    elif int(ch)==9:
        os.system("ssh {}  exit()".format(ip))
    elif int(ch)==0:
        command = input("Enter the command: ")
        os.system(command)
    elif int(ch)==10:
        from menussh import sshmenu
        break
    else:
        print("Error!!!!\nNo supported action selected \nContact the developer")