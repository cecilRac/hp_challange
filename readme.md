Start server in learning mode: python honeypot_cecil.py --learn
    This mode creates a file to track all scanners.

Start server in protect mode: python honeypot_cecil.py --protect
    This mode checks all visits to info stored in the file created by the learning mode.

using this module in another script:
    Accessible functions :
        server(address->string,port->int,arg_mode->int)
            This function is used to start a new server.
            arg_mode can be 0 or any other number. By default it is 0.
            0 represents --learn mode and 1 (or any other number) is for protect mode

        To use the methods below make sure there is a storage file named 'blackList.txt' in the directory

        learn(scanner_ip->string, user_agent->string):
            This function is to record new scanner information into the file system.
            scanner_ip is the new id you want recorded.
            user_agent is the Opreating System (os) the scanner runs.

        protect(scanner_ip->string, user_agent->string):
            This function is to crosscheck with the file we have stored after 'learning' for some time.
            scanner_ip is the ip address you want to verify if it has visited the server before.
            user_agent is the Opreating System (os) the scanner runs.