import socket
import time

ip = "127.0.0.1"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 50000))
#PORTS = [ 21, 22, 80, 443, 4444 ]
#def portscan(ip, times=0, timeout=0.5):
#    start_time = time.time()
#    
#    try:
#        socket.inet_aton(ip)
#    except socket.error:
#        return 'Error: Invalid IP address.'
#
#    results = ''
#
#    for p in PORTS:
#        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#        c = s.connect_ex((ip, p))
#        socket.setdefaulttimeout(timeout)
#
#        state = 'open' if not c else 'closed'
#
#        results += '{:>5}/tcp {:>10}\n'.format(p, state)
#        time.sleep(times)
#
#    end_time = time.time()
#    elapsed = end_time - start_time
#    print("Elapsed time: {}".format(elapsed))
#
#    return results
#
#if __name__ == "__main__":
#    ports = portscan(ip)
#    print(ports)
