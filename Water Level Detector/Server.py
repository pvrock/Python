import socket
import datetime
import pickle
from threading import Thread
class clienthandler:
    
    def getrequest(self):
        conn,addr=s.accept()
        while True:
            waiting=1;
            while True:
                try:
                    key=conn.recv(1024)
                    break
                except:
                    if waiting==1:
                        print("Waiting For Client")
                        waiting+=1;
            if key!=b'123456':
                conn.sendall(b'INVALID KEY')
                conn.close()
                getrequest()
            else:
                conn.sendall(b'valid key')
                
            alreadyconn.append(addr)
            print(now.now(),'live:',alreadyconn)
            f=open('live.txt','a')
            f.write(str(now.now())+' --> '+str(alreadyconn)+'\n')
            f.close()
            print('connected to:',addr)
            while True:
                try:
                    l=conn.recv(1024)
                    l=pickle.loads(l)
                except:
                    print('CLENT LEFT ')
                    conn.close()
                    break
                sendtime=now.replace(hour=l[0], minute=l[1], second=l[2])
                print(str(sendtime))
                conn.sendall(b'time is set')
                break

now = datetime.datetime.now()
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=''
port=8009
s.bind((host,port))
s.listen(1)
l=[]
alreadyconn=[]
print("server .......")
for i in range(2):
    c=clienthandler()
    Thread(target=c.getrequest).start()
