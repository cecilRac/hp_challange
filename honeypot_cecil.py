#Author: Cecil Arthur (cecil.arthur@epita.fr)
#Description: honeypot with 2 primary modes; learn and recognize(protect)

import socket, os, sys, SocketServer
from ua_parser import user_agent_parser

filename = 'blackList.txt'
mode = 0
class TCPHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        self.header = self.request.recv(1024).strip()

        user_agent = self.header[self.header.find('User-Agent:'): ]
        user_agent = user_agent[ user_agent.find(' ') + 1 : user_agent.find('\r')]
        user_agent = user_agent_parser.Parse(user_agent)

        if mode == 0:
            learn(self.client_address[0], user_agent['os']['family'])
        else:
            protect(self.client_address[0], user_agent['os']['family'])

def server(address,port=8000,arg_mode=0):
    global mode
    mode = arg_mode
    try:
        if not os.path.exists(filename):
            fileObject = open(filename,'w')
            fileObject.close()
        httpServer = SocketServer.TCPServer((address, port), TCPHandler)
        print 'listening on ' + address + ':' + str(port) +'\n '
        httpServer.serve_forever()
    except KeyboardInterrupt as e:
        httpServer.server_close()
        print('Shutdown: ' + str(e))

def learn(scanner_ip, user_agent):
    match = 0
    print('visited by ' + scanner_ip + ' - ' + user_agent+'\n ')
    with open(filename) as file:
        for ip in file:
            ip = ip[:-1]
            if scanner_ip + '-' + user_agent == ip:
                match = 1
                break
    if match == 0:
        fileObject = open(filename,'a')
        fileObject.write(scanner_ip + '-' + user_agent +'\n')
        fileObject.close()

def protect (scanner_ip, user_agent):
    with open(filename) as file:
        for ip in file:
            ip = ip[:-1]
            if scanner_ip + '-' + user_agent == ip:
                print('** Detected Scanner ** ' + scanner_ip + ' - ' + user_agent+'\n')
                break

def main(arg):
    if not arg:
        print ' ** Argument expected :/ **'
    elif arg[0] == '--learn':
        server(socket.gethostbyname(socket.gethostname()))
    elif arg[0] == '--protect':
        server(socket.gethostbyname(socket.gethostname()),8000,1)
    else:
        print 'unknown argument passed'

if __name__ == "__main__":
    main(sys.argv[1:])