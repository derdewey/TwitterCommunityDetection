#!/usr/bin/env python2.5
"""
Remove 2.5 from the line above, its a hack needed for it to work on Fedora

Author: Akshay Bhat
Desc:  mapepr script which reverse id's in each pair, such that all lines will be sorted according to the id of the user following other user

ToDo: clear up the naming, current naming convention assumes reverse to be true

Usage: give
-mapper "mapper.py Reverse" 
for twitter dataset from KAIST
and just
-mapper mapper.py
for
SourceID\tTargetID\n
file 

"""
import sys

if __name__ == '__main__':
    Exclude = {}
    Reverse = False
    try: 
	for line in file('exclude.txt').readlines():
            Exclude[line.strip().split('\t')[0]] = 1
    except:
	pass
    if len(sys.argv) > 1:
        Reverse = True
    
    for line in sys.stdin:
        entries =  line.strip().split('\t')
        Following = entries[0]
        User = entries[1]
        if Exclude:
            if not(User in Exclude) and not(Following in Exclude):
                if Reverse:
                    print User + '\t' + Following
                else:
                    print Following + '\t' + User
        else:
            if Reverse:
                print User + '\t' + Following
            else:
                print Following + '\t' + User

