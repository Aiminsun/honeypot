#!/usr/bin/python
import socket
import sys
import argparse
import signal
from datetime import datetime
import time
import errno

class Configuration:
    port=23
    filename=""
    username="Username:"
    password="Password:"
    message="\n"
    output="output.log"
    ip="0.0.0.0"
    attempts=5
    denied="Access denied\n"

    def load_message(self):
        if self.filename!="":
            file=open(self.filename,'r')
            self.message=file.read()
            file.close()
        else:
            print ("no filename is loaded")
    def log_login_attempt(self,output):
        file=open(self.output,"a")
        file.write(output+"\n")
        file.close()

config = Configuration()

def signal_handler(signal,frame):
    global loop
    loop=0
    global connection
    connection.close()
    print ("\nStopping. Thanks for using.")
    print ("Please visit https://github.com/timgold81/")
    print ("contact timgold@gmail.com\n")


signal.signal(signal.SIGINT,signal_handler)

parser=argparse.ArgumentParser(description="Simple honey pod for telnet CLI net\
work connections attempts")
parser.add_argument("-p","--port",help="Port number to listen for connections. \
Default: 23")
parser.add_argument("-f","--filename",help="Text file name with welcome message\
 to be sent to the attacker. Default: No filename fill be loaded and no message\
 will be displayed")
parser.add_argument("-u","--username",help="Promt that will be sent to attacker\
 to ask for username. Default: \"Username:\"")
parser.add_argument("-w","--password",help="Promt that will be sent to attacker\
 to ask for password. Default: \"Password:\"")
parser.add_argument("-o","--output",help="Output file to log login attempts. \
Default: output.log")
parser.add_argument("-I","--ip",help="Bind to specific IP. Default: localhost")
parser.add_argument("-a","--attempts",help="Connections attempts counter. \
Default: 5")
parser.add_argument("-d","--denied",help="Fail message to send to attacker. \
Default: \"Access denied\"")
args=parser.parse_args()

if args.port:
    config.port=int(args.port)

if args.filename:
    config.filename=args.filename
    config.load_message()

if args.username:
    config.username=args.username+"\n"

if args.password:
    config.password=args.password+"\n"

if args.output:
    config.output=args.Output

if args.ip:
    config.ip=args.ip

if args.attempts:
    config.attempts=int(args.attempts)

if args.denied:
    config.denied=args.denied +"\n"

loop=1
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind((config.ip,config.port))
sock.listen(1)
while loop:
    connection, client_addr=sock.accept()
    config.log_login_attempt(str(datetime.now())+" Logged in: "+str(client_addr)+"\n")
    connection.sendall(config.message)
    try:
        for i in range(1,config.attempts):
            time.sleep(0.5)
            connection.sendall(config.username)
            data=connection.recv(255)
            if data:
                config.log_login_attempt(str(datetime.now())+", Username recieved: "+data)
            else:
                break
            time.sleep(0.5)
            connection.sendall(config.password)
            data=connection.recv(255)
            if data:
                config.log_login_attempt(str(datetime.now())+", Password recieved: "+data)
                connection.sendall(config.denied)
            else:
                break
        connection.close()
    except socket.error as e:
        config.log_login_attempt(str(datetime.now())+" Connection closed")
        connection.close()
    finally:
        connection.close()
