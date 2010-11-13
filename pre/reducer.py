#!/usr/bin/env python2.5
"""

Author: Akshay Bhat
Desc: reducer script to collect all ids followed by a user into a single line

"""
import sys

if __name__ == '__main__':
    curUser = None
    Buf = ''
    for line in sys.stdin:
        entries =  line.strip().split('\t')
        User = entries[0]
        Following = entries[1]
        if curUser != User:
            if curUser:
                print Buf
            Buf = User
            curUser = User
            Buf += '\t' + Following
        else:
            Buf += '\t' + Following
    print Buf
    

