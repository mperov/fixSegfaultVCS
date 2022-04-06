#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Copyright (c) 2022 Maksim Perov <coder@frtk.ru>
#

import sys

BUF_SIZE = 1024
ORIGIN_BYTES = b'\xe8\xf3\xfd\xff\xff\xff\xc8'
NEW_BYTES = b'\x90\x90\x90\x90\x90'

def patch(path2lib, addresses):
    with open(path2lib, 'r+b') as fh:
        for address in addresses:
            fh.seek(address)
            fh.write(NEW_BYTES)
            print(path2lib + ' is patched by ' + str(NEW_BYTES) + ' on position - ' + hex(address))

if __name__ == "__main__":
    if len (sys.argv) < 2:
        print("usage: ./patcher.py /path/to/library.so")
        sys.exit(-1)

    path2lib = sys.argv[1]

    try:
        with open(path2lib, 'rb') as fh:
            first4 = fh.read(4)
            if first4 != b'\x7fELF':
                print(path2lib + " isn't ELF file!")
                sys.exit(-1)
    except Exception as e:
        print(str(e))
        sys.exit(-1)

    print("library - " + path2lib)

    addresses = []
    address = 0
    count_match = 0
    with open(path2lib, 'rb') as fh:
        while True:
            buf = fh.read(BUF_SIZE)
            if buf:
                for byte in buf:
                    if byte == ORIGIN_BYTES[count_match]:
                        count_match += 1
                        if count_match == len(ORIGIN_BYTES):
                            print(str(ORIGIN_BYTES) + ' is found!')
                            addr = address - len(ORIGIN_BYTES) + 1
                            print('Address is ' + hex(addr))
                            addresses.append(addr)
                            count_match = 0
                    else:
                        count_match = 0
                    address += 1
            else:
                break

    patch(path2lib, addresses)
