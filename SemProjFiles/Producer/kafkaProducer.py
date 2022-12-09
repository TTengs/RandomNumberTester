import gzip
import json
from kafka import KafkaProducer

#NOTE Dockerfile does not work, so instead run script locally with python
#NOTE Prerequisite to run the script locally is to use VPN, have SSH to Node1 in VSCode and portforwarded 9094
producer = KafkaProducer(bootstrap_servers=['localhost:9094'], api_version=(2, 5, 0), value_serializer=lambda v: json.dumps(v).encode('utf-8'))
# Filter function

#send "historical data"
with gzip.open('./2015-01-01-15.json.gz', mode='rt', encoding='utf-8') as f:
    for line in f:
        jsonLine = json.loads(line)
        if "issue" in jsonLine["type"].str.lower()
            producer.send('test', value=jsonLine, key=str(jsonLine["repo"]["id"]).encode('utf-8')) 


# select_words = lambda s : s[1] > 400

# files = "hdfs://namenode:9000/stream-in/"
# # Read in all files in the directory
# txtFiles = sc.wholeTextFiles(files, 20)
# # Take the content of the files and split them
# all_word = txtFiles.flatMap(lambda s: s[1].split())
# # Change from list of words to list of (word, 1)
# word_map = all_word.map(lambda s: (s, 1))
# # Merge values with equal keys
# word_reduce = word_map.reduceByKey(lambda s, t: s+t)
# # Filter using the defined lambda and sort by value
# top_words = word_reduce.filter(select_words).sortBy(lambda s: s[1])
# # Save as text file
# top_words.saveAsTextFile('hdfs://namenode:9000/txt-out')
# # Collect to a Python list and print
# print(top_words.collect())
