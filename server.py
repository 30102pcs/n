import socket
#server IP & port
server_ip = '127.0.0.1'
port = 9999

server = socket.socket()

server.bind((server_ip,port))
server.listen(1)
print('----Server is ready----')

client, adder = server.accept()
print('----Client is cinnected----')

msg = client.recv(1024)
print('----Message received----')
print(msg)

client.send(b'Hi Hi i\'m sever.You\re name is:'+msg)
print('----Message send----')

client.close()
server.close()