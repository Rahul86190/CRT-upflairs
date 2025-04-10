import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip_add="192.168.160.70"
port=1234
complete=(ip_add,port)
# s.connect(complete)
message=input("Enter a Message")
encode_msg=message.encode("ascii")
s.sendto(encode_msg,complete)