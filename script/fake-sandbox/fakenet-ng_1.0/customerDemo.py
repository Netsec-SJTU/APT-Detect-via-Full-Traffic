import os #导入OS模块
import socket
import time
from ftplib import FTP
time.sleep(5)
HOST = '192.168.10.1'
PORT = 10888
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
data = "发送病毒编号"
while data:
    s.sendall(data.encode('utf-8'))
    data = s.recv(512)
    data=data.decode('utf-8')
    break
s.close()
bingdu='start C:\\Users\\Administrator\\Desktop\\bingdu\\'+data+'.exe'
f=open('C:\\Users\\Administrator\\Desktop\\NO.bat','w')
f.write(bingdu)
f.close()
os.system('C:\\Users\\Administrator\\Desktop\\运行.bat')

time.sleep(10)
os.system('C:\\Users\\Administrator\\Desktop\\NO.bat')
time.sleep(60)
os.system('C:\\Users\\Administrator\\Desktop\\kill.bat')
time.sleep(2)
files=os.listdir(".")
for filename in files:
    portion = os.path.splitext(filename)
    if portion[1]==".pcap":
        newname = data + ".pcap"
        os.rename(filename,newname)
        ftp=FTP() 
        ftp.set_debuglevel(0)   #打开调试级别;0为关闭调试信息 
        ftp.connect('192.168.10.1',21)  #连接FTP服务器 
        ftp.login('quchunchao','qcc62575665')   #登录，如果匿名登录则用空串代替即可
        bufsize = 1024  #设置缓冲块大小 
        file_handler = open('C:\\Users\\Administrator\\Desktop\\fakenet-ng_1.0\\'+newname,'rb')  #以读模式在本地打开文件 
        ftp.storbinary('STOR %s' % os.path.basename(newname),file_handler,bufsize) #上传文件 
        ftp.set_debuglevel(0) 
        file_handler.close() 
        ftp.quit() 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
data = '病毒分析完毕'
while data:
    s.sendall(data.encode('utf-8'))
    break
s.close()
os.system('C:\\Users\\Administrator\\Desktop\\poweroff.bat')


