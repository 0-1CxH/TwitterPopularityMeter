# Twitter Popularity Meter (using Mapreduce)
A mapreduce project that measures the popularity of a topic (hashtag) in a period of time.

## Design
### Twitter Streaming
Dependency: tweepy

Code: [streaming.py](streaming.py)

This piece of code gets tweet streams using tweepy, and stores extended tweet json objects in file. (Modified slightly from the example code of the tweepy library)

### Mapreduce Job
Dependency: json, hadoop (version: 2.7.7 (hadoop-streaming-2.7.7.jar))

Code: [map.py](map.py), [reduce.py](reduce.py)

Command line:
> STREAM_JAR_PATH='/usr/local/src/hadoop-2.7.7/share/hadoop/tools/lib/hadoop-streaming-2.7.7.jar' \
 HADOOP_PATH jar STREAM_JAR_PATH
-file '/opt/hadoop/home/hadoop8/pmeter/map.py' -file  '/opt/hadoop/home/hadoop8/pmeter/reduce.py' \
-mapper "python /opt/hadoop/home/hadoop8/pmeter/map.py" -reducer "python /opt/hadoop/home/hadoop8/pmeter/reduce.py" \
-input '/opt/hadoop/home/hadoop8/pmeter/input.txt' -output '/opt/hadoop/home/hadoop8/pmeter/result' 

Mapper reads the files that contains json objects, and extract the count of retweet, reply, quote and favorite for each tweet, then emits tuple (hashtag, count). Reducer adds all the numbers of same hashtag as raw popularity.

During this project, 4 streaming files are used as input of mapreduce job:
> 2019-12-12 05:33 /opt/hadoop/home/hadoop8/pmeter/Dec10.txt 2.8 G \
 2019-12-12 06:59 /opt/hadoop/home/hadoop8/pmeter/Dec11.txt 2.6 G\
2019-12-12 21:33 /opt/hadoop/home/hadoop8/pmeter/Dec12.txt 16.6 G \
2019-12-13 00:43 /opt/hadoop/home/hadoop8/pmeter/Dec12_2.txt 2.3 G 

### Normalizing Data

Code: [norm.py](norm.py)

The raw popularity should be normalized before further analysis. The file size is positively related to streaming time, so normalize count by file size represents the density in terms of time.

## Results
Raw popularity results (Resulta of Mapreduce) of each data file:
[Dec10.part-00000](raw_popularity/result_Dec10/), 
[Dec11.part-00000](raw_popularity/result_Dec11/), 
[Dec12.part-00000](raw_popularity/result_Dec12/), 
[Dec12_2.part-00000](raw_popularity/result_Dec12_2/)

Normalized popularity result:
[Normalized Popularity](NormalizedPopularity.txt)







