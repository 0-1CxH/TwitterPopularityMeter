

HADOOP_PATH='/usr/local/src/hadoop-2.7.7/bin/hadoop'

STREAM_JAR_PATH='/usr/local/src/hadoop-2.7.7/share/hadoop/tools/lib/hadoop-streaming-2.7.7.jar'

HADOOP_PATH jar STREAM_JAR_PATH \
-file '/opt/hadoop/home/hadoop8/pmeter/map.py' -file  '/opt/hadoop/home/hadoop8/pmeter/reduce.py' \
-mapper "python /opt/hadoop/home/hadoop8/pmeter/map.py" -reducer "python /opt/hadoop/home/hadoop8/pmeter/reduce.py" \
-input '/opt/hadoop/home/hadoop8/pmeter/Dec10.txt' -output '/opt/hadoop/home/hadoop8/pmeter/result' 
