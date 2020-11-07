import subprocess
import os
def awslocal():
    pass
print("\t\t\tWelcome to AWS cloud Control")
while True:
    print("\n\nList of AWS commands available")
    print("\tpress 1 for checking instacnes in environment ")
    print("\tpress 2 for checking Keys in environment with instacnes ")
    print("\tpress 3 for launching instance  in environment ")
    print("\tpress 4 checking keys in environment")
    print("\tPress 5 for launching EBS volume")
    print("\tEnter 6 for checking volume in environment by voulme id")
    print("\tEnter 7 for attaching EBS volume to an specific instacnes ")
    print("\tEnter 0 to enter the command yourself")
    print("\tPress 10 to go back to previous menu")
    x = int(input(" \n Enter your choice "))
    if x == 1:
      out1 =  subprocess.getoutput("aws ec2 describe-instances --query 'Reservations[*]'.'Instances[*]'.'[InstanceId]' ")
      print("your instacnes \n")
      print(out1)
    elif x == 2:
      out1 =  subprocess.getoutput("aws ec2 describe-instances --query 'Reservations[*]'.'Instances[*]'.'[KeyName]' ")
      print("your keys with instacnes \n")
      print(out1)
    elif x == 3:
      id1 = input("Enter image id: ")
      instancetype1 = input("Enter instace type: ")
      count1 = int(input("Enter how many os you want: "))
      subid = input("Enter subnet id: ")
      sec= input("Enter security group id: ")
      keyn= input("Enter key name: ")
      out1 =  subprocess.getoutput("aws ec2 run-instances --image-id {} --instance-type {} --count {} --subnet-id {} --security-group-ids {} --key-name {} ".format(id1,instancetype1,count1,subid,sec,keyn))
      print("your instacnes launched.. \n")
      print(out1)
    elif x == 4:
      out1 =  subprocess.getoutput("aws ec2 describe-key-pairs --query 'KeyPairs[*]'.'KeyName' ")
      print("your keys  \n")
      print(out1)
    elif x == 5:
      gb = int(input("Enter how much space you want in GB: "))
      out1 =  subprocess.getoutput("aws ec2 create-volume --volume-type gp2 --size {} --availability-zone ap-south-1 ".format(gb))
      print("\n")
      print(out1)
    elif 	x== 6:
      out1 =  subprocess.getoutput("aws ec2 describe-volumes --query 'Volumes[*]'.'['VolumeId','State']'")
      print("your Volumes  \n")
      print(out1)
      
    elif 	x==7:
      vid = input("Enter volume id : ")
      inid = input("Enter instacne id in which you want to connect: ")
      out1 =  subprocess.getoutput("aws ec2 attach-volume --volume-id {} --instance-id {} --device /dev/sdf ".format(vid,inid))
      print(out1)
    elif x == 0:
      command = input("Enter the command: ")
      os.system(command)
    elif (x == 10):
      from menulocal import localmenu
      break
    else:
      print("Error!!!!\nNo supported action selected \nContact the developer")
