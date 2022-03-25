#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Copyright (c) 2022 Maksim Perov <coder@frtk.ru>
#

import sys
import mmap

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
    #with open(path2lib, 'rb') as fh:
    #    fh.find(b'\xe8\xf3\xfd\xff\xff\xff\xc8')
    #    bytes4 = fh.read(4)
    #    print(bytes4)
