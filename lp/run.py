#!/usr/bin/env python
"""
Author: Akshay U. Bhat
    Description: Python file for setting up and executing Label Propgation job
    example call ./run.py Net.txt 4 17000000
	TO DO: wriete a custom partitionar instead of setting reducer to 1 
"""
import sys,os
exec_init_string = 'hadoop jar /usr/local/hadoop/contrib/streaming/hadoop-0.19.2-streaming.jar  -input %s -output %s.Label%d.txt -mapper "mapper.py %d" -reducer NONE -file mapper.py'
exec_string = 'hadoop jar /usr/local/hadoop/contrib/streaming/hadoop-0.19.2-streaming.jar  -input %s -output %s.Label%d.txt -mapper "mapper.py %d Label.txt" -reducer NONE -file mapper.py -file Label.txt'
exec_final_string = 'hadoop jar /usr/local/hadoop/contrib/streaming/hadoop-0.19.2-streaming.jar  -input %s.Label%d.txt -output %s.Label.final.txt -mapper "endmapper.py users.txt 70000000"  -reducer reducer.py -file reducer.py -file endmapper.py -file ../../users.txt'

get_string = 'hadoop fs -getmerge &.Label#.txt Label.txt'

if __name__ == '__main__':
    sizehint = 0
    infile = ''
    iterations = 0
    predict = False
    try:
        infile = sys.argv[1]
        iterations =  int(sys.argv[2])
        sizehint = int(sys.argv[3])
    except:
        print "Please specify infile, number of iterations, maximum node index"
        raise
    # run the mapper with all nodes with labels same as node id
    os.system(exec_init_string%(infile,infile,0,sizehint))
    # download the new Labels file
    os.system(get_string.replace('#','0').replace('&',infile))
    
    for i in range(1,iterations):
        os.system(exec_string%(infile,infile,i,sizehint))
        os.system('rm Label.txt')
        os.system(get_string.replace('#',str(i)).replace('&',infile))
    os.system(exec_final_string%(infile,i,infile))
    os.system('rm Label.txt')
