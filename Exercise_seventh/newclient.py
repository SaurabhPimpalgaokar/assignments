import socket
import sys
import argparse

#first create a client socket
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#ip ="192.168.42.164"
#port = 59448

parser = argparse.ArgumentParser()
parser.add_argument("ip",help="Enter IP address of localhost")
parser.add_argument("port",help="Enter port number")
args=parser.parse_args()


#after creating a socket , request connection to server
client_socket.connect((args.ip,int(args.port)))


def client_send_data():
    message_to_server = input("Enter request to Server : ")
    client_socket.send(str.encode(message_to_server))


def client_receive_data():
        received_data = client_socket.recv(1024)
        print("Server message : ",received_data.decode("utf-8"))
       
def func():
     while True :
        client_receive_data()    
        choice = input("Want to request to server : y/n ")
        if (choice =='y' or choice =='Y'):
            client_send_data()
        else:
            break

func()
client_socket.close()
    
