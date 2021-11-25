from speedtest import Speedtest
st=Speedtest()
print("Your Connection's Download Speed is: ",st.download())
print("Your Connection's Upload Speed is: ",st.upload())

#Make Sure that "pip install speedtest-cli" is already installed in order to run this Program
