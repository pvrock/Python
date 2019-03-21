import socket
import datetime
import pickle
host='localhost'
port=8009
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
l=[]
while True:
    l=[]
    s.send(b'123456')
    verify=s.recv(1024)
    if verify!=b'valid key':
        print(verify)
        break
    print(verify)
    hr=int(input("Enter hours: "))
    minute=int(input("Enter min: "))
    sec=int(input("Enter sec: "))
    l.append(hr)
    l.append(minute)
    l.append(sec)
    l=pickle.dumps(l)
    s.send(l)
    recieved=s.recv(1024)
    print(recieved)
    test=input("DO YOU WANNA EXIT: (Y/N) ")
    if test=='Y' or test=='y':
        break
s.close()
