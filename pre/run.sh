#!/usr/bin/env sh
# Generic Usage:
# ./run.sh DP
hadoop jar /usr/local/hadoop/contrib/streaming/hadoop-0.19.2-streaming.jar -input $1 -output $1.net -mapper mapper.py -reducer reducer.py -file mapper.py -file reducer.py 

# for twitter
#hadoop jar /usr/local/hadoop/contrib/streaming/hadoop-0.19.2-streaming.jar -input $1 -output $1.net -mapper 'mapper.py Reverse' -reducer reducer.py -file mapper.py -file reducer.py -file exclude.txt