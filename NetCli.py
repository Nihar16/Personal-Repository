import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

host = socket.gethostname()    
#host='172.16.56.200'                       

port = 12345

# connection to hostname on the port.
s.connect((host, port))                               

# Receive no more than 1024 bytes
msg = s.recv(1024)                                     
print (msg.decode('ascii'))
msg = input("Request: ")
s.send(msg.encode('ascii'))
msg = s.recv(1024)                                     
print (msg.decode('ascii'))
s.close()
