# Extracting logs with flume send to kafka and store in postgresql with Docker

## Overview
Application that sends the logs from /var/logs/messages and var/log/httpd/ access_logs.
We use flume to send the logs to kafka and a script in python was developed to save the logs in postgres


## Installation

1. Clone the repository ` git clone https://github.com/Dauzy/FlumeToKafka.git ` 

2. We're create a python virtual enviroment
... `python3.x -m venv evn` or `virtual -p python 3.x env`
... `source env/bin/activate` and `pip install -r requirements.txt`

3. 
