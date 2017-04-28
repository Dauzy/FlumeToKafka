# Extracting logs with flume send to kafka and store in postgresql

## Overview
Application that sends the logs from /var/logs/messages and var/log/httpd/ access_logs.
We use flume to send the logs to kafka and a script in python was developed to save the logs in postgres
