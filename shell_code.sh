#!/bin/bash

if [ -z "$HADOOP_HOME" ]; then
    echo "HADOOP_HOME is not set. Please set it and try again."
    exit 1
fi

hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.6.jar wordcount /input /output_1
echo "Wordcount job finished."

hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.6.jar sort /input_sort /output_sort_1
echo "Sort job finished."

hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.6.jar grep /input /output_2 'error'
echo "Grep job finished."
