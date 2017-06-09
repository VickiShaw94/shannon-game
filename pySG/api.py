
from __future__ import print_function
from shannonGame import shannon as sh
import sys
import zerorpc

class Shannon(object):
    def shannon(self):
       return sh()

def parse_port():
    return 4242

def main():
    addr = 'tcp://127.0.0.1:' + str(parse_port())
    s = zerorpc.Server(Shannon())
    s.bind(addr)
    print('start running on {}'.format(addr))
    s.run()

if __name__ == '__main__':
    main()

