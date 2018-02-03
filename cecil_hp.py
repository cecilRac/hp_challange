from socket import socket, AF_INET, SOCK_STREAM
import os
import SimpleHTTPServer
import SocketServer

filename = 'blackList.txt'
def server(address,port=9600,mode=1):
    try:

        handler = SimpleHTTPServer.SimpleHTTPRequestHandler

        httpServer = SocketServer.TCPServer((address, port), handler)
        print 'listening on ' + address + ':' + str(port) +'\n ';
        httpServer.serve_forever()

        #overload/overwrite serve_forever() function.
        '''
        if not os.path.exists(filename):
            fileObject = open(filename,'w')
            fileObject.close();

        while True:
            
            connection,scanner_address = server_socket.accept();
            #print('visited by ' + scanner_address[0] + ':' +str(scanner_address[1]) +'\n ');
            if scanner_address[0]: 
                if mode == 0:  
                    learn(scanner_address[0]);
                else:
                    protect(scanner_address[0]);     '''

    except KeyboardInterrupt as e:
        server_socket.Shutdown()
        server_socket.close()
        print('Shutdown: ' + str(e))

def learn(scanner_ip):
    match = 0;
    print('visited by ' + scanner_address[0] +'\n ');
    with open(filename) as file:
        for ip in file:
            ip = ip[:-1];
            if scanner_ip == ip:
                print('ip '+ ip)
                print('sc '+ scanner_ip)
                match = 1 
                break

    if match == 0:
        fileObject = open(filename,'a')
        fileObject.write(scanner_ip+'\n')
        fileObject.close()   


def protect (scanner_ip):
    with open(filename) as file:
        for ip in file:
            ip = ip[:-1];
            if scanner_ip == ip:
                print('* Detected Scanner * ' + scanner_ip +'\n');
                break;
                  

server('192.168.1.2');


        
        #TODO: get user agent of client;
        #TODO: make this a module
        #create file for keeping track. of clinet address - user agents.



