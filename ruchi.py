import time
	import datetime
	import psutil as p
	import platform
	from getmac import get_mac_address     
	import os
	import subprocess
	import sys
	

	user_input='''
	Press 1 to Check current time and Date :- 
	Press 2 to Check RAM Size of Your current OS  :- 
	Press 3 to KNow Name of YOur current OS :- 
	Press 4 to Check What is MAc Address of YOur lapTOP/PC/VM/CLoudVM :- 
	Press 5 to create one directory IN your Desktop :- 
	Press 6 to Restart Your current OS :- 
	Press 7 to Print list of all available Wifi in your laptop Range :-
	Press 8 to RUn another code in Your current folder  :-  
	Press 9 to exit the programe :- 
	'''
	print(user_input)
	# to accept input from user 
	user_choice=input()
	# printing user input 
	print("user has entered ",user_choice)
	

	def size(bytes, suffix="B"):
	    
	    #Scale bytes to its proper format
	   
	    factor = 1024
	    for unit in ["", "K", "M", "G", "T", "P"]:
	        if bytes < factor:
	            return f"{bytes:.2f}{unit}{suffix}"
	        bytes /= factor
	def memory():
	  mem = p.virtual_memory()
	  print("Total Memory:    ",size(mem.total))
	  print("Available Memory:", size(mem.available))
	  print("Used Memory:     ", size(mem.used))
	  print("Percentage:      ",mem.percent,"% \n")
	if  user_choice ==  '1' :
	    print("current date  and time is : " ,datetime.datetime.now())
	    
	    
	elif  user_choice  ==  '2' :
	    memory()
	

	elif user_choice == '3':
	    print("Name of the OS system:",platform.system())
	

	elif user_choice ==  '4':
	    print("Mac address of my system : " ,get_mac_address())
	

	elif user_choice== '5' :
	    dir_path="C:/Users/Education/Desktop/"
	    dir_name = input("Enter directory name: ")
	    path = os.path.join(dir_path,dir_name)
	    os.mkdir(path)
	    print("Directory '% s' created" % dir_name)
	elif user_choice=='6':
	    os.system("shutdown /r /t 1")
	elif user_choice=='7':
	    devices = subprocess.check_output(['netsh','wlan','show','network'])
	  
	    # decode it to strings
	    devices = devices.decode('ascii')
	    devices= devices.replace("\r","")
	    print(devices)
	elif user_choice== '8':
	    os.system('python task1.py')
	elif user_choice == '9':
	    sys.exit("program done")
