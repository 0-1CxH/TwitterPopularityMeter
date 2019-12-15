# Twitter Popularity Meter (using Mapreduce)
A mapreduce project that measures the popularity of a topic (hashtag) in a period of time.

## Design
### Twitter Streaming
Dependency: tweepy

Code: [streaming.py](streaming.py)

Twitter Credentials are obtained on  https://apps.twitter.com/ 

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
>  /opt/hadoop/home/hadoop8/pmeter/Dec10.txt 2.8 G \
 /opt/hadoop/home/hadoop8/pmeter/Dec11.txt 2.6 G\
 /opt/hadoop/home/hadoop8/pmeter/Dec12.txt 16.6 G \
 /opt/hadoop/home/hadoop8/pmeter/Dec12_2.txt 2.3 G 

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

The result suggests that the following 20 hashtags are the most popular during Dec.10 - Dec.12, 2019:


JIMIN	6.93640840983\
TIMEPOY	6.79616347482\
BeBest	4.49561358864\
BTS	2.77895580243\
InTheHeightsMovie	1.97859533954\
RedVelvet	1.75234050018\
레드벨벳	1.71586787995\
RVF	1.7154933867\
Sad	1.4626868109\
Summer2020	1.42203202941\
ARMY	1.38941178679\
SpotifyWrapped	1.35607575292\
Spotify	1.35326042085\
우리아미상받았네	1.33558303091\
クリスマスボックス	1.33438669853\
Jungkook	1.25850981651\
ローソン	1.07708727688\
エルチキ	1.05218529347\
Lチキ無料プレゼント	1.05205537558\
HopeOnTheStreet	1.01107578993\





