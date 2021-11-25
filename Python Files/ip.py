
def identify(block):
	if(block<=127):
		return('A','255.0.0.0')
	elif(block<=191):
		return('B','255.255.0.0')
	elif(block<=223):
		return('C','255.255.255.0')
	elif(block<=239):
		return('D','255.255.255.255')
	else:
		return('E','255.255.255.255')

def test(block):
	for i in block:
		if(int(i)>255):
			return(False)
	return(True)

def mask(ipb,submask,splchar):
	subm = submask.split(splchar)
	netip = ipb  = ipb.split(splchar)

	for i in range(0,len(ipb)):
		netip[i] = str(int(ipb[i])&int(subm[i]))
		
	return(splchar.join(netip))

while(True):
	try:
		choice = int(input("\n1.Dotted Decimal\n2.Binary\n3.Exit\n\nChoice:"))
		if(choice==1):
			ip = input("\nIP Address: ")
			block = ip.split('.')
			if(test(block)):

				ipclass,subnetmask = identify(int(block[0]))
				print("Class:",ipclass)
				print("SubnetMask:",subnetmask)

				netid = mask(ip,subnetmask,'.')
				print("NetworkID:",netid)
			else:
				print("\nInvalid IP Address!")

		if(choice==2):
			ip = input("\nIP Address: ")
			block = ip.split(' ')
			decblock = [str(int(i,2)) for i in block]
			if(test(decblock)):

				ipclass,subnetmask = identify(int(decblock[0]))
				print("Class:",ipclass)

				binsubmask = [bin(int(i))[2:] for i in subnetmask.split('.')]
				print("SubnetMask:"," ".join(binsubmask))

				netid = mask(".".join(decblock),subnetmask,'.')

				binnetid = [bin(int(i))[2:] for i in netid.split('.')]
				print("NetworkID:"," ".join(binnetid))
			else:
				print("\nInvalid IP Address!")

		if(choice>=3):
			break
	except:
		print("\nInvalid Argument!")