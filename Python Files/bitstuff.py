
#---------------sender site----------------------

frame = raw_input("\nEnter Data: ")

#print frame
print("\nBefore Stuffing: "+frame+"\n")

for i in range(0,len(frame)):
	if(frame[i:i+6]=="011111"):
		frame = frame[:i+6]+"0"+frame[i+6:]

#flag append
flag = " 01111110 "

#print dataframe after flags
print("\nBitstuffed Frame: "+flag+frame+flag)

#---------------reciever site---------------------

for i in range(0,len(frame)):
	if(frame[i:i+6]=="011111"):
		frame = frame[:i+6]+frame[i+7:]

#print dataframe removing flags & stuffed bits
print("\nRecovered Frame: "+frame+"\n")

