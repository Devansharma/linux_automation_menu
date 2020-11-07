import os

def lvmssh():
    pass

print("\t\t\tWelocome to LVM via ssh")
ip = input("Type the IP you want to run LVM on: ")

while True:
    print("""Press 1 to create a Physical Volume
             Press 2 to create a Volume Group 
             Press 3 to create a Logical Volume 
             Press 4 to Extend the Storage Capacity of Data Node by 5GB 
             Press 0 to type the command yourself
             Press 10 to go back to previous menu
    """)
    n=int(input("Enter your choice: "))
    if (n==1):
        os.system("ssh {0} pvcreate /dev/sdc".format(ip))
        os.system("ssh {0} pvcreate /dev/sdb".format(ip))
        print("PV CREATED!!")
    elif (n==2):
        os.system("ssh {0} vgcreate hadoopSto /dev/sdb /dev/sdc".format(ip))
        print("VG CREATED!!")
    elif n==3:
        os.system("ssh {0} lvcreate --size 50G --name hadoopLV hadoopSto".format(ip))
        os.system("ssh {0} mkfs.ext4 /dev/hadoopSto/hadoopLV".format(ip))
        os.system("ssh {0} mkdir hadoopdrive".format(ip))
        os.system("ssh {0} mount /dev/hadoopSto/hadoopLV /hadoopdrive".format(ip))
    elif n==4:
        os.system("ssh {0} lvextend --size +5G /dev/hadoopSto/hadoopLV".format(ip))
        os.system("ssh {0} resize2fs /dev/hadoopSto/hadoopLV".format(ip))
    elif(n == 0):
        command = input("Enter the command: ")
        os.system("ssh {0} {1}".format(ip,command))
    elif(n == 10):
        from menussh import sshmenu
        break
    else:
        print("Error!!!!\nNo supported action selected \nContact the developer")