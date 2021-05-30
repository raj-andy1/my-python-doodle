#python script to measure time taken to create any atlassian stack using cloudformation and get it fully up and running.
import requests
import time
import datetime
import sys
import signal
import logging
import validators
import boto3
import botocore
from urllib.parse import urlparse

delete_response_list = ['CREATE_FAILED','DELETE_COMPLETE','DELETE_FAILED','DELETE_IN_PROGRESS','REVIEW_IN_PROGRESS','ROLLBACK_COMPLETE','ROLLBACK_IN_PROGRESS','ROLLBACK_FAILED']

def keyboardInterruptHandler(signal,frame):
	#log.debug('Received keyboard interrupt, Exiting')
	print('Exiting due to interrupt')
	exit(0)

def is_url_present():
	try:
		url = sys.argv[1]
	except IndexError:
		print ('Pls provide input url, exiting...')
		#print (url)
		exit(0)
	return url

def get_stack_name():
	url = is_url_present()
	print (url)
	if validators.url(url):
		'''for a valid URL using url parse determine the stackname from the URL, aws cfn stackname is of the form stackname.domainname
		so we need to split the domain'''
		stacknm = urlparse(url).hostname
		stacknm = stacknm[:stacknm.find('.')] #find the first period and get the hostname before the first period
		#print (stacknm)
	else:
		print ('URL Validation Failed for: ' + is_url_present() + '. Please check URL and try again')
		print (validators.url(url))
		exit(0)
	return stacknm

def get_stack_creation_time(stackname):
	client = boto3.client('cloudformation', region_name=sys.argv[2])
	stacknm = get_stack_name()


signal.signal(signal.SIGINT, keyboardInterruptHandler)


client = boto3.client('cloudformation', region_name=sys.argv[2])
url = is_url_present()
stacknm = get_stack_name()
count = 0
serviceFlag = True

while True:
	try:
		response = client.describe_stacks(
			StackName = stacknm)
			#print (response['Stacks'][0]['StackStatus'])
		if response['Stacks'][0]['StackStatus'] == 'CREATE_IN_PROGRESS':
			print ('Creation of stack: ' + stacknm + ' is in progress' + ' *** ' + str(datetime.datetime.now().replace(microsecond=0)))
			serviceFlag = True
			time.sleep(10)
			continue
		elif response['Stacks'][0]['StackStatus'] in delete_response_list:
			print ('Received Error %s in creating stack %s ,exiting...' % (response['Stacks'][0]['StackStatus'], stacknm))
			exit(0)
		elif response['Stacks'][0]['StackStatus'] == 'CREATE_COMPLETE':
			response = client.describe_stack_events(
				StackName = stacknm)
			stack_creation_time = response['StackEvents'][0]['Timestamp'] - response['StackEvents'][-1]['Timestamp']
			print ('%s Stack has been created' % stacknm)
			print ('Time taken to create the stack - %s is %s:' % (stacknm, stack_creation_time))
			break
		else:
			print ('Stack - %s creation status is %s which is currently not supported, exiting...' % (stacknm,  response['Stacks'][0]['StackStatus']))
			exit(0)
	except botocore.exceptions.ClientError as e:
		print (e)
		exit(0)
#print (serviceFlag)

while serviceFlag:
	print ('Trying to connect to the service url:', url)
	start_time = datetime.datetime.now().replace(microsecond=0)
	while count < 100:
		try:
			r = requests.get(url)
		except requests.exceptions.RequestException as e:
			print('Error connecting to' + url + 'Response Code:' +  e + ' *** ' + str(datetime.datetime.now().replace(microsecond=0)))
			#print (e)
			time.sleep(10)
			count += 1
		else:
			print ('Status code for provided URL:' + url + ' is: ' + str(r.status_code))
			if (r.status_code == requests.codes.ok):
				serviceFlag == False
				print ('***Instance is up***')
				elapsed_time = datetime.datetime.now().replace(microsecond=0) - start_time
				print ('Total time for the instance to come up(hh:mm:ss):', elapsed_time)
				exit(0)
	print ('Exceeded number of tries, Exiting...')
	exit(0)


