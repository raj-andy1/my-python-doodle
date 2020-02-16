#!/bin/bash

yum update -y
yum install httpd -y

AZ=$(curl http://169.254.169.254/latest/meta-data/placement/availability-zone)
INST_ID=$(curl http://169.254.169.254/latest/meta-data/instance-id)
touch /var/www/html/index.html
echo "<html><body><center><h1>Hello Cloud Gurus. Here is my web page from $INST_ID in $AZ</h1></center></body></html>" > /var/www/html/index.html
touch /var/www/html/status.html
echo "<html><body><center><h1>Status is running</h1></center></body></html>" > /var/www/html/status.html

systemctl start httpd
systemctl enable httpd
