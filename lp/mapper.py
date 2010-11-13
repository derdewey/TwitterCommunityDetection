#!/usr/bin/python2.6


"""
Mapper for Label Propagation algorithm using map-reduce

Author:
Name:       Akshay Bhat
WebSite:    http://www.akshaybhat.com

"""
import os, random, time, sys, array, logging, collections

def ParseOptions(argv):
    """
    Parse the Command line Options
    """
    SizeHint = 0
    if len(argv) > 1:
        SizeHint = int(argv[1])
    if len(argv) > 2:
        Labels = argv[2]
    else:
        Labels  = ''
    return [SizeHint,Labels]


def ApplyAndVote(line,delim = '\t'):
    """
    Applies the value of label for each neighbor
    and calls maxVote function
    """
    entry =  line.strip().split(delim)
    del line
    node = int(entry[0])
    
    if len(entry) != 1:     # handles cases where a node is not connected to any other node
        nLabels = [Label[int(k)] for k in entry[1:]]
        newLabel, weight = maxVote(nLabels) 
        return node, newLabel, weight 
    else:
        return node, node, 1


def maxVote(nLabels):
    """
    This function is used byt map function, given a list of labels of neighbors
    this function finds the most frequent labels and randomly returns one of them
    """
    cnt = collections.defaultdict(int)
    for i in nLabels:
        cnt[i] += 1
    maxv = max(cnt.itervalues())
    weight =  float(maxv) / len(nLabels)
    return random.choice([k for k,v in cnt.iteritems() if v == maxv]), weight

                
if __name__ == '__main__':
    [SizeHint,Labels]=ParseOptions(sys.argv) # Parse the command line options
    Label = range(SizeHint) # according to a post on stackoverflow this is faster than array.array, confirmed it myself as well   
    if Labels:
        for line in file(Labels):
            entries = line.strip().split('\t') 
            Label[int(entries[0])] = int(entries[1])
    for line in sys.stdin:
        try:
            node, newLabel, weight = ApplyAndVote(line)
            print str(node) + '\t' + str(newLabel) +'\t' +str(weight)
        except:
            print line
            raise
