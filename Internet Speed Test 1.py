from speedtest import Speedtest
st=Speedtest()
option=int(input(''' What speed do you want to test:
1]Download Speed
2]Upload Speed
3]Ping'''))
if option == 1: 
    print(st.download())
elif option == 2:
    print(st.upload())
elif option == 3:
    servernames=[]
    st.get_server(servernames)
    print(st.results.ping)
else:
    print("Please Enter a valid Choice!")
    
