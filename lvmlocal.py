import os

def lvmlocal():
    pass

print("\t\t\tTo Provide Elasticity to Data Node Storage")
while True:
    print("""\tPress 1 to create a Physical Volume
             Press 2 to create a Volume Group 
             Press 3 to create a Logical Volume 
             Press 4 to Extend the Storage Capacity of Data Node by 5GB 
             Press 0 to type the command yourself
             Press 10 to go back to previous menu
    """)

    n=int(input("Enter your choice: "))
    if (n==1):
        os.system("pvcreate /dev/sdc")
        os.system("pvcreate /dev/sdb")
        print("PV CREATED!!")
    elif (n==2):
        os.system("vgcreate hadoopSto /dev/sdb /dev/sdc")
        print("VG CREATED!!")
    elif (n==3):
        os.system("lvcreate --size 50G --name hadoopLV hadoopSto")
        os.system("mkfs.ext4 /dev/hadoopSto/hadoopLV")
        os.system("mkdir hadoopdrive")
        os.system("mount /dev/hadoopSto/hadoopLV /hadoopdrive")
    elif (n==4):
        os.system("lvextend --size +5G /dev/hadoopSto/hadoopLV")
        os.system("resize2fs /dev/hadoopSto/hadoopLV")
    elif(n == 0):
        command = input("Enter the command: ")
        os.system(command)
    elif(n == 10):
        from menulocal import localmenu
        break
    else:
        print("Error!!!!\nNo supported action selected \nContact the developer")