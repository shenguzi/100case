# -*- coding: UTF-8 -*-
import socket               # 导入 socket 模块

s = socket.socket()         # 创建 socket 对象
host = socket.gethostname() # 获取本地主机名
print ("host",host)
port = 12345 # 设置端口
host= "127.0.0.1"
s.bind((host, port))        # 绑定端口

s.listen(5)                 # 等待客户端连接
sendata="this is a test你好" \
        "地球人"
while True:
    c, addr = s.accept()     # 建立客户端连接。
    print ('连接地址：', addr)
    c.sendall(bytes(sendata,encoding='utf8'))
    c.close()                # 关闭连接

try:
    c.close()
finally:
    print("exit")