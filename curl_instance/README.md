# curl_jira.py
This python program 'pings' an instance which can respond to a http request and measures the time it took for the response.

essentially I created this program to measure the time it took for me from the point I hit the 'Submit' button on AWS Cloudformation console to the time the instance was provisioned and the service running.

# Usage
`python3 curl_jira.py <url>`
_*example*_
`python3 curl_jira.py http://ar-jira-dc-01.teamsin.space`