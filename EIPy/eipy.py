#!/usr/bin/env python
from string import ascii_uppercase, ascii_lowercase, digits, punctuation
import argparse

parser = argparse.ArgumentParser(description='For use in finding EIP offsets')
group = parser.add_argument_group('required argument')
group.add_argument('-l', '--length', dest='length', type=int,
                   help='length of the string', required=True, metavar='')
parser.add_argument('-q', '--query', dest='query',
                    help='find the EIP offset in bytes', metavar='')
parser.add_argument('-e', '--exclude', dest='exclude',
                    help='provide characters to exclude', metavar='',
                    default='')
args = parser.parse_args()

u = filter(lambda x: x not in args.exclude, ascii_uppercase)
l = filter(lambda x: x not in args.exclude, ascii_lowercase)
d = filter(lambda x: x not in args.exclude, digits)
p = filter(lambda x: x not in args.exclude, punctuation)


def generate(length):
    s = []
    for i in range(0, length):
        s.append(u[i % len(u)])
        s.append(l[i % len(l)])
        s.append(d[i % len(d)])
        s.append(p[i % len(p)])
    return ''.join(s)


def query(s, hex_string):
    hex_string = hex_string.strip('0x')
    # The following should work for all versions of Python
    decoded =''.join(chr(int(hex_string[i:i+2], 16)) for i in range(0, len(hex_string), 2))
    offset = s.find(decoded)
    if offset == -1:
        print('[!] EIP offset not found')
    else:
        print('[+] EIP offset located at {} bytes'.format(offset))


def main():
    s = generate(args.length)
    if args.query:
        query(s, args.query)
    else:
        print('\n' + s)

if __name__ == '__main__':
    main()
