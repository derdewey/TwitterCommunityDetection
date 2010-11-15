#!/usr/bin/env sh
# Generic Usage:
# ./run-twitter.sh twitter_rv.net

cd ..
cd pre
hadoop jar /usr/local/hadoop/contrib/streaming/hadoop-0.19.2-streaming.jar -input $1 -output Twitter/Net.pegasus -mapper 'mapper.py Reverse' -reducer NONE -file mapper.py
hadoop jar /usr/local/hadoop/contrib/streaming/hadoop-0.19.2-streaming.jar -input $1 -output Twitter/Net.exclude -mapper 'mapper.py Reverse' -reducer reducer.py -file mapper.py -file reducer.py -file ../twitter/exclude.txt
hadoop jar /usr/local/hadoop/contrib/streaming/hadoop-0.19.2-streaming.jar -input $1 -output Twitter/Net.complete -mapper 'mapper.py Reverse' -reducer reducer.py -file mapper.py -file reducer.py
cd ..

cd lp
./run.py Twitter/Net.exclude 15 70000000 
cd ..




# cd ../PEG
# code for perfoming in/out degree and page rank calculation using Pegasus
# ./run_dd.sh in 72 Twitter/Net.pegasus
# ./run_dd.sh out 72 Twitter/Net.pegasus
# ./run_pr.sh 72 70000000 nosym Twitter/Net.pegasus
# cd ..
