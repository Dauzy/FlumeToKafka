# Extracting logs with flume send to kafka and store in postgresql with Docker

## Overview
Application that sends the logs from /var/logs/messages and var/log/httpd/ access_logs.
We use flume to send the logs to kafka and a script in python was developed to save the logs in postgres


## Installation

1. Clone the repository `git clone https://github.com/Dauzy/FlumeToKafka.git ` 

2. We're create a python virtual enviroment
... `python3.x -m venv evn` or `virtual -p python 3.x env`
... `source env/bin/activate` and `pip install -r requirements.txt`

3. Run kafka docker image and postgres docker images
... `sudo docker run -it -p 2181:2181 -p 9092:9092 --env ADVERTISED_HOST=localhost --env ADVERTISED_PORT=9092 spotify/kafka`
... `sudo docker run --name name-postgres -e POSTGRES_PASSWORD=mysecretpassword -d  -p 5432:5432 postgres`

4. Download [Apache Flume] (http://www.apache.org/dyn/closer.lua/flume/1.7.0/apache-flume-1.7.0-bin.tar.gz)
... `tar -xzf apache-flume-x.x.x.x-bin.tar.gz` 
... Enter to apache-flume-1.7.0-bin/conf and run the follow command: 
...`sudo /bin/flume-ng agent --name source_agent --conf ./conf/ --conf-file conf/flume-log-kafka.conf -Dflume.root.logger=DEBUG,console`

5. Check that docker container are running `sudo docker run ps`, that show you the kafka and postgres containers

6. Enter to postgres client and create tables that are in  tables.txt
...`docker run -it --rm --link name-of-your-postgres-docker-container:postgres postgres psql -h postgres`

Until this point you only have to enter ConsumerPost.py and PyPost.py to adjust the connection parameters 
of postgres and kafka and after run COnsumerPost.py.


Happy code!!
