import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip_add="192.168.160.70"
port=1234
complete=(ip_add,port)
s.bind(complete)
while True:
    message=s.recvfrom(1024)
    decoded_msg=message[0].decode("ascii")
    print(decoded_msg)