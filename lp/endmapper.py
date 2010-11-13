#!/usr/bin/python2.6


"""
Mapper for Label Propagation algorithm using map-reduce

Author:
Name:       Akshay Bhat
WebSite:    http://www.akshaybhat.com

"""
import sys
                
if __name__ == '__main__':
    try:
            filename = sys.argv[1]
            names = ['']*int(sys.argv[2])
            for line in file(filename):
                try:
                    line = line.strip().split(' ')
                    names[int(line[0])] = line[1]
                except:
                    pass
    except:
        raise
    for line in sys.stdin:
        try:
            node = int(line.strip().split('\t')[0])
            label = int(line.strip().split('\t')[1])
            score = line.strip().split('\t')[2]
            if names:
                if names[node]:
                    node = names[node]
                if names[label]:
                    label = names[label]
            print str(label)+'\t'+str(node)+'\t'+score
        except:
            print line
            raise
