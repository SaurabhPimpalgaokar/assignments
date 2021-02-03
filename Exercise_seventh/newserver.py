import socket
import sys
from _thread import *
import argparse
thread_number = 0
global output
#first create a server socket
#AF_INET is type and sock_Stream is for tcp mode
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

parser = argparse.ArgumentParser()
parser.add_argument("-ip",help="Enter IP address of localhost")
parser.add_argument("-port",help="Enter port number ")
args=parser.parse_args()

#ip = "192.168.42.164"
#port = 59448

#after creating a socket , bind the socket to ip address and port 
try :
    server_socket.bind((args.ip,int(args.port)))
except socket.error as e:
    print(str(e))
    sys.exit()


#server goes to listen mode
server_socket.listen(5)


def server_send_data(connection,message_to_client):
    connection.send(str.encode(message_to_client))                  #encode the message to be sent


def server_receive_data(connection):
    received_data = connection.recv(1024)                           # receive data upto 1024 bytes
    print("Client message: ",received_data.decode("utf-8"))         # decode the message
    return received_data.decode("utf-8")                            # decode the message while return to function

def client_thread(connection):                                   
        dictionary={'PING':'PING_OK','LIST':'LIST_OK','HELLO':'WORLD','QUIT':'QUIT_ERR'}
        while True :
            data = server_receive_data(connection)                      # receive data from client
            if not data :                                               # stop if data not received
                sys.exit()
            if data in dictionary:                                      
                server_send_data(connection,dictionary[data])           #send corresponding value(data) if key found in dictionary
            else:
                server_send_data(connection,"UNKNOWN_CMD")              #send respind as unknown if request is other than the element in dictionary 
                   
while True :
    #start connection with client
    client,address = server_socket.accept()                         #accept method starts connection with client and return client_object with address
    start_new_thread(client_thread,(client,))                       # new connection thread starts for new client
    print(f"listening at {address}")                                # fstring can be used here 
    client.send(str.encode("Server Listening: "))                   # server send message to client to confirm the connection established or not
    thread_number += 1
    print("number of connections : ",str(thread_number)) 
server_socket.close()




