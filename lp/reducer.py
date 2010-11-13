#!/usr/bin/env python
"""

Description: Reducer used to summarize the results

Used for summarizing results into following format. Provide input only from endmapper.py,
also sort only based on node as key, else  a single cluster might get split into two different reducers. 

cluster-label \t num_nodes \t  nodeid \t weight \t  nodeid \t weight ...... 
"""
import sys

if __name__ == '__main__':
        oldcommunity = ''
        temp = ''
        count = 0
        community = ''
        for line in sys.stdin:  # line must be output from end mapper sorted on label as key, 
                entries = line.strip().split('\t')
                community = entries[0]
                node = entries[1]
                weight = entries[2]
                if community != oldcommunity or count==10000:
                        if oldcommunity:
                                print oldcommunity+'\t'+str(count)+'\t'+temp
                        oldcommunity = community
                        temp = node + '\t' + weight
                        count = 1
                else:
                        count += 1
                        temp += '\t' + node + '\t' + weight
        if community:
                print community+'\t'+str(count)+'\t'+temp

