import socket
import sys  
  
try: 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    print("Socket successfully created")
except socket.error as err: 
    print("socket creation failed with error %s" %(err)) 
  
port = 80
sitename=input("Enter Website Name: ")
try: 
    host_ip = socket.gethostbyname(sitename) 
except socket.gaierror: 
  
    print("There was an error resolving the host")
else:
   s.connect((host_ip, port)) 
   print("The socket has successfully connected to :", sitename)
   print("At IP Address == %s" %(host_ip))
