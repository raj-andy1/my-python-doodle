#sample code to test out the instances

import boto3
import requests
import validators
import signal
import sys


j8dc_stack_list = ['jira-002', 'jira-003', 'jira-004', 'jira-005', 'jira-006', 'jira-007', 'jira-008', 'jira-009', 'jira-010', 'jira-011', 'jira-012', 'jira-013', 'jira-014', 'jira-015', 'jira-016', 'jira-017', 'jira-018', 'jira-019', 'jira-020', 'jira-021', 'jira-022', 'jira-023', 'jira-024', 'jira-025', 'jira-026', 'jira-027', 'jira-028', 'jira-029', 'jira-030', 'jira-031', 'jira-032', 'jira-033', 'jira-034', 'jira-035', 'jira-036', 'jira-037', 'jira-038', 'jira-039', 'jira-040', 'jira-041', 'jira-042', 'jira-043', 'jira-044', 'jira-045', 'jira-046', 'jira-047', 'jira-048', 'jira-049', 'jira-050', 'jira-051', 'jira-052', 'jira-053', 'jira-054', 'jira-055', 'jira-056', 'jira-057', 'jira-058', 'jira-059', 'jira-060', 'jira-061']
domain_nm = 'open.atlassian.guru'
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
		full_url = 'http://' + url + ':' + str(port)
	else:
		full_url = 'http://' + url
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