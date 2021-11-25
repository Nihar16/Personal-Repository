import socket                
  
s = socket.socket()          
print("Creating Socket .... Done")

port = 12345                
  
s.bind(('', port))         
print("Binding Socket to %s port ..... Done" %(port))
  
#Making Socket to listen to the Network
s.listen(5)      
print("socket is Now listening .....")            
done1=1 
while done1 != 0: 
   c, addr = s.accept()      
   print ("Got connection from", addr) 
  
   # send a thank you message to the client.  
   sstr="Thank you for connecting .... Host: IP Address: "+str(addr[0])+"\r\n"
   c.send(sstr.encode('ascii')) 
   sstr=c.recv(1024)
   print(sstr.decode('ascii'))
   if sstr.decode('ascii') == 'Send Data':
       sstr="Data Packet: 'ABCDEFGHIJK' ....\r\n"
       c.send(sstr.encode('ascii'))
   else:
       sstr="Ok ... But for Now closing ....\r\n"
       c.send(sstr.encode('ascii'))
       
       done1=int(input("Done (0 - Yes): "))
       if done1=="":
           done1=1
   
   # Close the connection with the client 
   c.close() 
s.close()
print("Closing Server Connection .... Done")