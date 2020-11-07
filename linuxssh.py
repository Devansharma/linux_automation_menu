import os

def linuxssh():
    pass

print("\t\t\tWelocome to linux via ssh")
ip = input("Type the IP you want to run LVM on: ")

while True:
    print("\n\nList of linux commands via ssh")
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
