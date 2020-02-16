#!/bin/bash

yum update -y
yum install httpd -y
service httpd start

AZ=$(curl http://169.254.169.254/latest/meta-data/placement/availability-zone)
INST_ID=$(curl http://169.254.169.254/latest/meta-data/instance-id)
echo "<html><body><center><h1>Hello Cloud Gurus. Here is my web page from $INST_ID in $AZ</h1></center></body></html>" > /var/www/html/index.html
