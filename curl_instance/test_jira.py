#sample code to test out the instances

import boto3
import requests
import validators
import signal
import sys


j8dc_stack_list = ['jira-backup-west-002', 'jira-backup-west-003', 'jira-backup-west-004', 'jira-backup-west-005', 'jira-backup-west-006', 'jira-backup-west-007', 'jira-backup-west-008', 'jira-backup-west-009', 'jira-backup-west-010', 'jira-backup-west-011', 'jira-backup-west-012', 'jira-backup-west-013', 'jira-backup-west-014', 'jira-backup-west-015', 'jira-backup-west-016', 'jira-backup-west-017']
domain_nm = 'pe.atlassian.camp'
j8dc_url_list = []
bad_url_list = []
good_url_list = []

port = ''

def keyboardInterruptHandler(signal,frame):
	#log.debug('Received keyboard interrupt, Exiting')
	print('Exiting due to interrupt')
	exit(0)

signal.signal(signal.SIGINT, keyboardInterruptHandler)

for stack in j8dc_stack_list:
	url = stack + '.' + domain_nm
	j8dc_url_list.append(url)

print (j8dc_url_list)


for url in j8dc_url_list:
	if port:
		full_url = 'https://' + url + ':' + str(port)
	else:
		full_url = 'https://' + url
	print ('New url is %s' % full_url)
	if validators.url(full_url):
		print ('Validation successful for %s' % full_url)
		print ('Trying %s' % full_url)
		try:
			r = requests.get(full_url)
		except requests.exceptions.RequestException as e:
			print ('Connection Error for url: %s' % full_url)
			bad_url_list.append(url)
		else:
			#print ('Status code for provided URL:' + full_url + ' is: ' + str(r.status_code))
			if (r.status_code == requests.codes.ok):
				print ('Connection Succesful for url: %s' %full_url)
				good_url_list.append(url)
	else:
		print ('Validation failed for %s' % url)
print ('List of NON working urls is: %s' % bad_url_list)
print ('List of working urls is: %s' % good_url_list)

exit(0)